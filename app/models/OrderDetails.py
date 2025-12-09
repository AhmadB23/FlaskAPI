from datetime import datetime
from app.models import db
import uuid

class OrderDetails(db.Model):
    __tablename__ = 'order_details'
    
    # BaseModel fields
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    # OrderDetails fields
    total_amount = db.Column(db.Numeric(18, 2), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    order_status = db.Column(db.String(20), nullable=False, default='Pending')  # Pending, Confirmed, Shipped, Delivered, Cancelled
    shipping_address = db.Column(db.String(255), nullable=False, default='')
    city = db.Column(db.String(100), nullable=False, default='')
    phone_number = db.Column(db.String(15), nullable=False, default='')
    
    # Foreign Key
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=True)
    
    # Relationships
    user = db.relationship('User', backref='orders', lazy=True)
    # Note: order_items relationship is defined via backref in OrderItem model
    
    def to_dict(self):
        return {
            'id': self.id,
            'total_amount': float(self.total_amount),
            'order_date': self.order_date.isoformat() if self.order_date else None,
            'order_status': self.order_status,
            'shipping_address': self.shipping_address,
            'city': self.city,
            'phone_number': self.phone_number,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
        }
