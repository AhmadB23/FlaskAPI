from app.models import db
from app.models.BaseModel import BaseModel

class OrderItem(BaseModel, db.Model):
    __tablename__ = 'order_items'
    
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
            **self.base_to_dict(),
            'unit_price': float(self.unit_price),
            'quantity': self.quantity,
            'user_id': self.user_id,
            'order_details_id': self.order_details_id,
            'book_id': self.book_id,
        }
