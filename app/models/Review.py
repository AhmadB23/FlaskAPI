from app.models import db
from app.models.BaseModel import BaseModel

class Review(BaseModel, db.Model):
    __tablename__ = 'reviews'
    
    # Review fields
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    comment = db.Column(db.Text, nullable=True)
    
    # Foreign Keys
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.String(36), db.ForeignKey('books.id'), nullable=False)
    
    # Relationships
    user = db.relationship('User', backref='reviews', lazy=True)
    book = db.relationship('Book', backref='reviews', lazy=True)
    
    def to_dict(self):
        return {
            **self.base_to_dict(),
            'rating': self.rating,
            'comment': self.comment,
            'user_id': self.user_id,
            'book_id': self.book_id,
        }
