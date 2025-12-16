from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.AuthorService import AuthorService
from app.models import User

author_bp = Blueprint("authors", __name__)

def is_admin():
    """Check if current user is admin (role >= 1)"""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return user and user.role >= 1

# GET all authors
@author_bp.route('/authors', methods=['GET'])
def get_authors():
    """Public endpoint to get all authors"""
    authors = AuthorService.get_all_authors()
    return jsonify([author.to_dict() for author in authors]), 200

# GET author by ID
@author_bp.route('/authors/<author_id>', methods=['GET'])
def get_author(author_id):
    """Get author by ID"""
    author = AuthorService.get_author_by_id(author_id)
    if not author:
        return jsonify({'error': 'Author not found'}), 404
    return jsonify(author.to_dict()), 200

# POST create author (Admin only)
@author_bp.route('/authors', methods=['POST'])
@jwt_required()
def create_author():
    """Create new author - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    try:
        data = request.get_json()
        if not data.get('author_name'):
            return jsonify({'error': 'Author name is required'}), 400
        
        author = AuthorService.create_author(data)
        return jsonify(author.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# PUT update author (Admin only)
@author_bp.route('/authors/<author_id>', methods=['PUT'])
@jwt_required()
def update_author(author_id):
    """Update author - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    try:
        data = request.get_json()
        author = AuthorService.update_author(author_id, data)
        if not author:
            return jsonify({'error': 'Author not found'}), 404
        return jsonify(author.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# DELETE author (Admin only)
@author_bp.route('/authors/<author_id>', methods=['DELETE'])
@jwt_required()
def delete_author(author_id):
    """Delete author - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    success = AuthorService.delete_author(author_id)
    if not success:
        return jsonify({'error': 'Author not found'}), 404
    return jsonify({'message': 'Author deleted successfully'}), 200

