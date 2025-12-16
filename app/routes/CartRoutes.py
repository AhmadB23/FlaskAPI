from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.CartService import CartService

cart_bp = Blueprint("cart", __name__)

# GET user's cart
@cart_bp.route('/cart', methods=['GET'])
@jwt_required()
def get_cart():
    """Get current user's cart"""
    current_user_id = get_jwt_identity()
    cart_items = CartService.get_user_cart(current_user_id)
    
    # Include book details and total
    cart_data = {
        'items': [item.to_dict() for item in cart_items],
        'total': CartService.get_cart_total(current_user_id)
    }
    
    return jsonify(cart_data), 200

# POST add item to cart
@cart_bp.route('/cart/items', methods=['POST'])
@jwt_required()
def add_to_cart():
    """Add item to cart"""
    try:
        current_user_id = get_jwt_identity()
        data = request.get_json()
        
        book_id = data.get('book_id')
        quantity = data.get('quantity', 1)
        
        if not book_id:
            return jsonify({'error': 'Book ID is required'}), 400
        
        if quantity < 1:
            return jsonify({'error': 'Quantity must be at least 1'}), 400
        
        cart_item = CartService.add_to_cart(current_user_id, book_id, quantity)
        return jsonify(cart_item.to_dict()), 201
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# PUT update cart item quantity
@cart_bp.route('/cart/items/<cart_item_id>', methods=['PUT'])
@jwt_required()
def update_cart_item(cart_item_id):
    """Update cart item quantity"""
    try:
        current_user_id = get_jwt_identity()
        data = request.get_json()
        
        quantity = data.get('quantity')
        if not quantity or quantity < 1:
            return jsonify({'error': 'Valid quantity is required'}), 400
        
        cart_item = CartService.update_cart_item(cart_item_id, current_user_id, quantity)
        if not cart_item:
            return jsonify({'error': 'Cart item not found'}), 404
        
        return jsonify(cart_item.to_dict()), 200
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# DELETE remove item from cart
@cart_bp.route('/cart/items/<cart_item_id>', methods=['DELETE'])
@jwt_required()
def remove_from_cart(cart_item_id):
    """Remove item from cart"""
    current_user_id = get_jwt_identity()
    success = CartService.remove_from_cart(cart_item_id, current_user_id)
    
    if not success:
        return jsonify({'error': 'Cart item not found'}), 404
    
    return jsonify({'message': 'Item removed from cart'}), 200

# DELETE clear entire cart
@cart_bp.route('/cart', methods=['DELETE'])
@jwt_required()
def clear_cart():
    """Clear all items from cart"""
    current_user_id = get_jwt_identity()
    CartService.clear_cart(current_user_id)
    return jsonify({'message': 'Cart cleared'}), 200
