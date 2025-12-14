from app.models import Book, db
from datetime import datetime

class BookService:
    
    @staticmethod
    def get_all_books(filters=None):
        """Get all active books with optional filters"""
        query = Book.query.filter_by(is_deleted=False)
        
        if filters:
            if filters.get('category_id'):
                query = query.filter_by(category_id=filters['category_id'])
            if filters.get('author_id'):
                query = query.filter_by(author_id=filters['author_id'])
            if filters.get('min_price'):
                query = query.filter(Book.price >= filters['min_price'])
            if filters.get('max_price'):
                query = query.filter(Book.price <= filters['max_price'])
        
        return query.all()
    
    @staticmethod
    def get_book_by_id(book_id):
        """Get book by ID"""
        return Book.query.filter_by(id=book_id, is_deleted=False).first()
    
    @staticmethod
    def create_book(data):
        """Create new book - Admin only"""
        new_book = Book(
            title=data['title'],
            isbn=data.get('isbn'),
            price=data['price'],
            stock_quantity=data.get('stock_quantity', 0),
            description=data.get('description'),
            author_id=data.get('author_id'),
            category_id=data.get('category_id'),
            created_by=data.get('created_by', '')
        )
        db.session.add(new_book)
        db.session.commit()
        return new_book
    
    @staticmethod
    def update_book(book_id, data):
        """Update existing book"""
        book = Book.query.filter_by(id=book_id, is_deleted=False).first()
        if not book:
            return None
        
        book.title = data.get('title', book.title)
        book.isbn = data.get('isbn', book.isbn)
        book.price = data.get('price', book.price)
        book.stock_quantity = data.get('stock_quantity', book.stock_quantity)
        book.description = data.get('description', book.description)
        book.author_id = data.get('author_id', book.author_id)
        book.category_id = data.get('category_id', book.category_id)
        book.updated_at = datetime.utcnow()
        
        db.session.commit()
        return book
    
    @staticmethod
    def delete_book(book_id):
        """Soft delete book"""
        book = Book.query.filter_by(id=book_id, is_deleted=False).first()
        if not book:
            return False
        
        book.is_deleted = True
        book.deleted_at = datetime.utcnow()
        db.session.commit()
        return True
    
    @staticmethod
    def check_stock(book_id, quantity):
        """Check if sufficient stock is available"""
        book = Book.query.filter_by(id=book_id, is_deleted=False).first()
        if not book:
            return False
        return book.stock_quantity >= quantity
    
    @staticmethod
    def reduce_stock(book_id, quantity):
        """Reduce stock after purchase - use in transaction"""
        book = Book.query.filter_by(id=book_id, is_deleted=False).with_for_update().first()
        if not book or book.stock_quantity < quantity:
            return False
        
        book.stock_quantity -= quantity
        db.session.commit()
        return True
