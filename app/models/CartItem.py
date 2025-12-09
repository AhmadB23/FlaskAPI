from datetime import datetime
from app.models import db
import uuid

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    
    # BaseModel fields
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    
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
            'id': self.id,
            'quantity': self.quantity,
            'book_id': self.book_id,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
        }
