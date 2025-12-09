from datetime import datetime
from app.models import db
import uuid

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    # BaseModel fields
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    # OrderItem fields
    unit_price = db.Column(db.Numeric(18, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    # Foreign Keys
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=True)
    order_details_id = db.Column(db.String(36), db.ForeignKey('order_details.id'), nullable=True)
    book_id = db.Column(db.String(36), db.ForeignKey('books.id'), nullable=True)
    
    # Relationships
    user = db.relationship('User', backref='order_items', lazy=True)
    order_details = db.relationship('OrderDetails', backref='order_items', lazy=True)
    book = db.relationship('Book', backref='order_items', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'unit_price': float(self.unit_price),
            'quantity': self.quantity,
            'user_id': self.user_id,
            'order_details_id': self.order_details_id,
            'book_id': self.book_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
        }
