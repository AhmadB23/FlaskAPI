from datetime import datetime
from app.models import db
import uuid

class CartHistory(db.Model):
    __tablename__ = 'cart_history'
    
    # BaseModel fields
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.now(datetime.timezone.utc))
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    # CartHistory fields
    quantity = db.Column(db.Integer, nullable=False)
    price_at_purchase = db.Column(db.Numeric(18, 2), nullable=False)
    
    # Foreign Keys
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=True)
    book_id = db.Column(db.String(36), db.ForeignKey('books.id'), nullable=True)
    order_item_id = db.Column(db.String(36), db.ForeignKey('order_items.id'), nullable=True)
    
    # Relationships
    user = db.relationship('User', backref='cart_histories', lazy=True)
    book = db.relationship('Book', backref='cart_histories', lazy=True)
    order_item = db.relationship('OrderItem', backref='cart_histories', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'price_at_purchase': float(self.price_at_purchase),
            'user_id': self.user_id,
            'book_id': self.book_id,
            'order_item_id': self.order_item_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
        }
