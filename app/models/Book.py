from app.models import db
from app.models.BaseModel import BaseModel

class Book(BaseModel, db.Model):
    __tablename__ = 'books'
    
    # Book-specific fields
    title = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(50), unique=True, nullable=True)
    price = db.Column(db.Numeric(18, 2), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.Text, nullable=True)
    
    # Foreign Keys
    author_id = db.Column(db.String(36), db.ForeignKey('authors.id'), nullable=True)
    category_id = db.Column(db.String(36), db.ForeignKey('categories.id'), nullable=True)
    
    def to_dict(self):
        return {
            **self.base_to_dict(),
            'title': self.title,
            'isbn': self.isbn,
            'price': float(self.price) if self.price else None,
            'stock_quantity': self.stock_quantity,
            'description': self.description,
            'author_id': self.author_id,
            'category_id': self.category_id,
        }
