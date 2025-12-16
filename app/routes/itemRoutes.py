from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.OrderService import OrderService
from app.models import User

# This blueprint is for Order Items (deprecated - use OrderRoutes instead)
# Kept for backward compatibility
items_bp = Blueprint('items', __name__)

def is_admin():
    """Check if current user is admin (role >= 1)"""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return user and user.role >= 1

@items_bp.route('/items', methods=['GET'])
@jwt_required()
def get_items():
    """Get all order items (Admin only) - Deprecated: Use /api/v1/admin/orders instead"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    orders = OrderService.get_all_orders()
    return jsonify([order.to_dict() for order in orders]), 200

@items_bp.route('/items/<item_id>', methods=['GET'])
@jwt_required()
def get_item(item_id):
    """Get order item by ID - Deprecated: Use /api/v1/orders/<order_id> instead"""
    current_user_id = get_jwt_identity()
    
    if is_admin():
        order = OrderService.get_order_by_id(item_id)
    else:
        order = OrderService.get_order_by_id(item_id, current_user_id)
    
    if not order:
        return jsonify({"error": "Item not found"}), 404
    
    return jsonify(order.to_dict()), 200

@items_bp.route('/items', methods=['POST'])
@jwt_required()
def create_item():
    """Create order - Deprecated: Use /api/v1/orders/checkout instead"""
    try:
        current_user_id = get_jwt_identity()
        data = request.get_json()
        
        order = OrderService.create_order_from_cart(current_user_id, data)
        return jsonify(order.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
