from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

book_bp = Blueprint("books", __name__)

# GET all books (with optional filters)
@book_bp.route('/books', methods=['GET'])
def get_books():
    """Get all books - Not implemented"""
    return jsonify({'message': 'Book module not implemented'}), 501

# GET book by ID
@book_bp.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    """Get book by ID - Not implemented"""
    return jsonify({'message': 'Book module not implemented'}), 501

# POST create book (Admin only)
@book_bp.route('/books', methods=['POST'])
@jwt_required()
def create_book():
    """Create book - Not implemented"""
    return jsonify({'message': 'Book module not implemented'}), 501

# PUT update book (Admin only)
@book_bp.route('/books/<book_id>', methods=['PUT'])
@jwt_required()
def update_book(book_id):
    """Update book - Not implemented"""
    return jsonify({'message': 'Book module not implemented'}), 501

# DELETE book (Admin only)
@book_bp.route('/books/<book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    """Delete book - Not implemented"""
    return jsonify({'message': 'Book module not implemented'}), 501
