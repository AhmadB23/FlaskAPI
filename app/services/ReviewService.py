from app.repositories.ReviewRepository import ReviewRepository
from typing import List, Dict, Optional

class ReviewService:
    """Service layer for Review business logic"""
    
    def __init__(self):
        self.repository = ReviewRepository()
    
    def create_review(self, user_id: str, book_id: str, rating: int, comment: str = None) -> Dict:
        """Create a new review"""
        # Validate rating
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        
        review_data = {
            'user_id': user_id,
            'book_id': book_id,
            'rating': rating,
            'comment': comment
        }
        
        review = self.repository.create(review_data)
        return review.to_dict()
    
    def get_review(self, review_id: str) -> Optional[Dict]:
        """Get review by ID"""
        review = self.repository.get_by_id(review_id)
        return review.to_dict() if review else None
    
    def get_all_reviews(self) -> List[Dict]:
        """Get all reviews"""
        reviews = self.repository.get_all()
        return [review.to_dict() for review in reviews]
    
    def get_book_reviews(self, book_id: str) -> List[Dict]:
        """Get all reviews for a book"""
        reviews = self.repository.get_by_book_id(book_id)
        return [review.to_dict() for review in reviews]
    
    def get_user_reviews(self, user_id: str) -> List[Dict]:
        """Get all reviews by a user"""
        reviews = self.repository.get_by_user_id(user_id)
        return [review.to_dict() for review in reviews]
    
    def update_review(self, review_id: str, update_data: Dict) -> Optional[Dict]:
        """Update a review"""
        review = self.repository.get_by_id(review_id)
        if not review:
            return None
        
        # Validate rating if provided
        if 'rating' in update_data and not 1 <= update_data['rating'] <= 5:
            raise ValueError("Rating must be between 1 and 5")
        
        updated_review = self.repository.update(review, update_data)
        return updated_review.to_dict()
    
    def delete_review(self, review_id: str) -> bool:
        """Delete a review"""
        review = self.repository.get_by_id(review_id)
        if not review:
            return False
        
        self.repository.delete(review)
        return True
