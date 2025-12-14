from app.models import db
from app.models.BaseModel import BaseModel

class CartItem(BaseModel, db.Model):
    __tablename__ = 'cart_items'
    
    # CartItem fields
    quantity = db.Column(db.Integer, nullable=False, default=1)
    
    # Foreign Keys
    book_id = db.Column(db.String(36), db.ForeignKey('books.id'), nullable=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=True)
    
    # Relationships
    book = db.relationship('Book', backref='cart_items', lazy=True)
    user = db.relationship('User', backref='cart_items', lazy=True)
    
    def to_dict(self):
        return {
            **self.base_to_dict(),
            'quantity': self.quantity,
            'book_id': self.book_id,
            'user_id': self.user_id,
        }
