from app.models import CartItem, Book, db
from datetime import datetime

class CartService:
    
    @staticmethod
    def get_user_cart(user_id):
        """Get all cart items for a user"""
        return CartItem.query.filter_by(user_id=user_id, is_deleted=False).all()
    
    @staticmethod
    def add_to_cart(user_id, book_id, quantity=1):
        """Add item to cart or update quantity if exists"""
        # Check if book exists and has stock
        book = Book.query.filter_by(id=book_id, is_deleted=False).first()
        if not book:
            raise ValueError('Book not found')
        
        if book.stock_quantity < quantity:
            raise ValueError(f'Insufficient stock. Available: {book.stock_quantity}')
        
        # Check if item already in cart
        cart_item = CartItem.query.filter_by(
            user_id=user_id, 
            book_id=book_id, 
            is_deleted=False
        ).first()
        
        if cart_item:
            # Update quantity
            new_quantity = cart_item.quantity + quantity
            if book.stock_quantity < new_quantity:
                raise ValueError(f'Insufficient stock. Available: {book.stock_quantity}')
            cart_item.quantity = new_quantity
            cart_item.updated_at = datetime.utcnow()
        else:
            # Create new cart item
            cart_item = CartItem(
                user_id=user_id,
                book_id=book_id,
                quantity=quantity
            )
            db.session.add(cart_item)
        
        db.session.commit()
        return cart_item
    
    @staticmethod
    def update_cart_item(cart_item_id, user_id, quantity):
        """Update cart item quantity"""
        cart_item = CartItem.query.filter_by(
            id=cart_item_id, 
            user_id=user_id, 
            is_deleted=False
        ).first()
        
        if not cart_item:
            return None
        
        # Check stock
        book = Book.query.get(cart_item.book_id)
        if book.stock_quantity < quantity:
            raise ValueError(f'Insufficient stock. Available: {book.stock_quantity}')
        
        cart_item.quantity = quantity
        cart_item.updated_at = datetime.utcnow()
        db.session.commit()
        return cart_item
    
    @staticmethod
    def remove_from_cart(cart_item_id, user_id):
        """Remove item from cart"""
        cart_item = CartItem.query.filter_by(
            id=cart_item_id, 
            user_id=user_id, 
            is_deleted=False
        ).first()
        
        if not cart_item:
            return False
        
        cart_item.is_deleted = True
        cart_item.deleted_at = datetime.utcnow()
        db.session.commit()
        return True
    
    @staticmethod
    def clear_cart(user_id):
        """Clear all items from user's cart"""
        cart_items = CartItem.query.filter_by(user_id=user_id, is_deleted=False).all()
        for item in cart_items:
            item.is_deleted = True
            item.deleted_at = datetime.utcnow()
        db.session.commit()
        return True
    
    @staticmethod
    def get_cart_total(user_id):
        """Calculate cart total"""
        cart_items = CartItem.query.filter_by(user_id=user_id, is_deleted=False).all()
        total = 0
        for item in cart_items:
            book = Book.query.get(item.book_id)
            if book:
                total += float(book.price) * item.quantity
        return total
