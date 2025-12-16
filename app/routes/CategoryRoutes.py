from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.CategoryService import CategoryService
from app.models import User

category_bp = Blueprint("categories", __name__)

def is_admin():
    """Check if current user is admin (role >= 1)"""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return user and user.role >= 1

# GET all categories
@category_bp.route('/categories', methods=['GET'])
def get_categories():
    """Public endpoint to get all categories"""
    categories = CategoryService.get_all_categories()
    return jsonify([category.to_dict() for category in categories]), 200

# GET category by ID
@category_bp.route('/categories/<category_id>', methods=['GET'])
def get_category(category_id):
    """Get category by ID"""
    category = CategoryService.get_category_by_id(category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    return jsonify(category.to_dict()), 200

# POST create category (Admin only)
@category_bp.route('/categories', methods=['POST'])
@jwt_required()
def create_category():
    """Create new category - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    try:
        data = request.get_json()
        if not data.get('category_type'):
            return jsonify({'error': 'Category type is required'}), 400
        
        category = CategoryService.create_category(data)
        return jsonify(category.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# PUT update category (Admin only)
@category_bp.route('/categories/<category_id>', methods=['PUT'])
@jwt_required()
def update_category(category_id):
    """Update category - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    try:
        data = request.get_json()
        category = CategoryService.update_category(category_id, data)
        if not category:
            return jsonify({'error': 'Category not found'}), 404
        return jsonify(category.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# DELETE category (Admin only)
@category_bp.route('/categories/<category_id>', methods=['DELETE'])
@jwt_required()
def delete_category(category_id):
    """Delete category - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    success = CategoryService.delete_category(category_id)
    if not success:
        return jsonify({'error': 'Category not found'}), 404
    return jsonify({'message': 'Category deleted successfully'}), 200
