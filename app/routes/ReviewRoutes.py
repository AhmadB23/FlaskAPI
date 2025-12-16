from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.ReviewService import ReviewService
from app.utils.enums import is_admin

review_bp = Blueprint('reviews', __name__)
review_service = ReviewService()

@review_bp.route('/', methods=['GET'])
def get_all_reviews():
    """Get all reviews"""
    reviews = review_service.get_all_reviews()
    return jsonify(reviews), 200

@review_bp.route('/<review_id>', methods=['GET'])
def get_review(review_id):
    """Get a specific review"""
    review = review_service.get_review(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review), 200

@review_bp.route('/book/<book_id>', methods=['GET'])
def get_book_reviews(book_id):
    """Get all reviews for a book"""
    reviews = review_service.get_book_reviews(book_id)
    return jsonify(reviews), 200

@review_bp.route('/user/<user_id>', methods=['GET'])
@jwt_required()
def get_user_reviews(user_id):
    """Get all reviews by a user"""
    current_user_id = get_jwt_identity()
    
    # Users can only view their own reviews unless admin
    if current_user_id != user_id and not is_admin():
        return jsonify({'error': 'Unauthorized'}), 403
    
    reviews = review_service.get_user_reviews(user_id)
    return jsonify(reviews), 200

@review_bp.route('/', methods=['POST'])
@jwt_required()
def create_review():
    """Create a new review"""
    data = request.get_json()
    user_id = get_jwt_identity()
    
    if not data.get('book_id') or not data.get('rating'):
        return jsonify({'error': 'book_id and rating are required'}), 400
    
    try:
        review = review_service.create_review(
            user_id=user_id,
            book_id=data['book_id'],
            rating=data['rating'],
            comment=data.get('comment')
        )
        return jsonify(review), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@review_bp.route('/<review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    """Update a review"""
    data = request.get_json()
    user_id = get_jwt_identity()
    
    # Check if review exists and belongs to user
    review = review_service.get_review(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    
    if review['user_id'] != user_id and not is_admin():
        return jsonify({'error': 'Unauthorized'}), 403
    
    try:
        updated_review = review_service.update_review(review_id, data)
        return jsonify(updated_review), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@review_bp.route('/<review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    """Delete a review"""
    user_id = get_jwt_identity()
    
    # Check if review exists and belongs to user
    review = review_service.get_review(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    
    if review['user_id'] != user_id and not is_admin():
        return jsonify({'error': 'Unauthorized'}), 403
    
    review_service.delete_review(review_id)
    return jsonify({'message': 'Review deleted successfully'}), 200
