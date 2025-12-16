from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.OrderService import OrderService
from app.models import User

order_bp = Blueprint("orders", __name__)

def is_admin():
    """Check if current user is admin (role >= 1)"""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return user and user.role >= 1

# POST checkout (create order from cart)
@order_bp.route('/orders/checkout', methods=['POST'])
@jwt_required()
def checkout():
    """Checkout - Create order from cart"""
    try:
        current_user_id = get_jwt_identity()
        data = request.get_json()
        
        # Validate shipping data
        if not data.get('shipping_address') or not data.get('city') or not data.get('phone_number'):
            return jsonify({'error': 'Shipping address, city, and phone number are required'}), 400
        
        order = OrderService.create_order_from_cart(current_user_id, data)
        
        return jsonify({
            'message': 'Order created successfully',
            'order': order.to_dict()
        }), 201
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# GET user's orders
@order_bp.route('/orders', methods=['GET'])
@jwt_required()
def get_user_orders():
    """Get all orders for current user"""
    current_user_id = get_jwt_identity()
    orders = OrderService.get_user_orders(current_user_id)
    return jsonify([order.to_dict() for order in orders]), 200

# GET order by ID
@order_bp.route('/orders/<order_id>', methods=['GET'])
@jwt_required()
def get_order(order_id):
    """Get order details by ID"""
    current_user_id = get_jwt_identity()
    
    # Check if admin - can view any order
    if is_admin():
        order = OrderService.get_order_by_id(order_id)
    else:
        # Regular user - can only view own orders
        order = OrderService.get_order_by_id(order_id, current_user_id)
    
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    
    # Get order items
    order_items = OrderService.get_order_items(order_id)
    
    return jsonify({
        'order': order.to_dict(),
        'items': [item.to_dict() for item in order_items]
    }), 200

# GET all orders (Admin only)
@order_bp.route('/admin/orders', methods=['GET'])
@jwt_required()
def get_all_orders():
    """Get all orders - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    orders = OrderService.get_all_orders()
    return jsonify([order.to_dict() for order in orders]), 200

# PUT update order status (Admin only)
@order_bp.route('/admin/orders/<order_id>/status', methods=['PUT'])
@jwt_required()
def update_order_status(order_id):
    """Update order status - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    try:
        data = request.get_json()
        status = data.get('status')
        
        if not status:
            return jsonify({'error': 'Status is required'}), 400
        
        order = OrderService.update_order_status(order_id, status)
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        
        return jsonify(order.to_dict()), 200
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400
