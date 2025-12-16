from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.BookService import BookService
from app.models import User, Review, db

book_bp = Blueprint("books", __name__)

def is_admin():
    """Check if current user is admin (role >= 1)"""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return user and user.role >= 1

# GET all books (with optional filters)
@book_bp.route('/books', methods=['GET'])
def get_books():
    """Public endpoint to browse books"""
    filters = {
        'category_id': request.args.get('category_id'),
        'author_id': request.args.get('author_id'),
        'min_price': request.args.get('min_price', type=float),
        'max_price': request.args.get('max_price', type=float)
    }
    
    books = BookService.get_all_books(filters)
    return jsonify([book.to_dict() for book in books]), 200

# GET book by ID
@book_bp.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    """Get book details by ID"""
    book = BookService.get_book_by_id(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book.to_dict()), 200

# POST create book (Admin only)
@book_bp.route('/books', methods=['POST'])
@jwt_required()
def create_book():
    """Create new book - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('title') or not data.get('price'):
            return jsonify({'error': 'Title and price are required'}), 400
        
        book = BookService.create_book(data)
        return jsonify(book.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# PUT update book (Admin only)
@book_bp.route('/books/<book_id>', methods=['PUT'])
@jwt_required()
def update_book(book_id):
    """Update book - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    try:
        data = request.get_json()
        book = BookService.update_book(book_id, data)
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        return jsonify(book.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# DELETE book (Admin only)
@book_bp.route('/books/<book_id>', methods=['DELETE'])
@jwt_required()
def delete_book(book_id):
    """Delete book - Admin only"""
    if not is_admin():
        return jsonify({'error': 'Admin access required'}), 403
    
    success = BookService.delete_book(book_id)
    if not success:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify({'message': 'Book deleted successfully'}), 200

# POST add review to book
@book_bp.route('/books/<book_id>/reviews', methods=['POST'])
@jwt_required()
def add_review(book_id):
    """Add review to a book"""
    try:
        current_user_id = get_jwt_identity()
        data = request.get_json()
        
        # Validate rating
        rating = data.get('rating')
        if not rating or rating < 1 or rating > 5:
            return jsonify({'error': 'Rating must be between 1 and 5'}), 400
        
        # Check if book exists
        book = BookService.get_book_by_id(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        
        # Create review
        review = Review(
            rating=rating,
            comment=data.get('comment', ''),
            user_id=current_user_id,
            book_id=book_id
        )
        db.session.add(review)
        db.session.commit()
        
        return jsonify(review.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# GET reviews for a book
@book_bp.route('/books/<book_id>/reviews', methods=['GET'])
def get_book_reviews(book_id):
    """Get all reviews for a book"""
    book = BookService.get_book_by_id(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    reviews = Review.query.filter_by(book_id=book_id, is_deleted=False).all()
    return jsonify([review.to_dict() for review in reviews]), 200
