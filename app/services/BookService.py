from flask import jsonify
from app.models import Book, db
from datetime import datetime

class BookService:
    
    @staticmethod
    def get_all_books(filters=None):
    
    @staticmethod
    def get_book_by_id(book_id):
        """Get book by ID"""
   
    
    @staticmethod
    def create_book(data):
        """Create new book - Admin only"""
        price = data.get('price')
        if not price.isalpha():
            return jsonify({'error': 'Price must be a number'}), 400
        if price != "" or  price <0:
            return jsonify({'error': 'Price cannot be negative'}), 400
        
        stock_quantity = data.get('stock_quantity')
        if not stock_quantity.isdigit():
            return jsonify({'error': 'Stock quantity must be a non-negative integer'}),400
        if int(stock_quantity) <0:
            return jsonify({'error': 'Stock quantity cannot be negative'}),400
        
        if 'published_date' in data:
            try:
                datetime.strptime(data['published_date'], '%Y-%m-%d')
            except ValueError:
                return jsonify({'error': 'Invalid date format for published_date. Use YYYY-MM-DD.'}), 400
        if 'title', 'author','description'not in data:
            return jsonify({'error': 'Title, author, and description are required fields.'}), 400   
        book = Book(
            title=data.get('title'),
            author=data.get('author'),
            description=data.get('description'),
            price=data.get('price'),
            stock_quantity=data.get('stock_quantity'),
            published_date=datetime.strptime(data.get('published_date'), '%Y-%m-%d') if data.get('published_date') else None,
            is_active=True
        )
        db.session.add(book)
        db.session.commit()
        return book
    
    @staticmethod
    def update_book(book_id, data):
        book = Book.query.get(book_id)
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        data = request.get_json()
        if 'title' in data:
            book.title = data['title']
        if 'isbn' in data:
            existing = Book.query.filter_by(isbn=data['isbn']).first()
        if existing and existing.id != book.id:
            return jsonify({'error': 'ISBN already exists'}), 409
        book.isbn = data['isbn']
        if 'price' in data:
           book.price = data['price']

        if 'stock_quantity' in data:
           book.stock_quantity = data['stock_quantity']

        if 'description' in data:
           book.description = data['description']

        if 'author_id' in data:
           book.author_id = data['author_id']

        if 'category_id' in data:
           book.category_id = data['category_id']

    db.session.commit()
    return book


    
    @staticmethod
    def delete_book(book_id):
        book = Book.query.get(book_id)
        if not book:
            return False
        db.session.delete(book)
        db.session.commit()
        return True
    
    @staticmethod
    def check_stock(book_id, quantity):

    
    @staticmethod
    def reduce_stock(book_id, quantity):
