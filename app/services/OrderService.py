from app.models import OrderDetails, OrderItem, CartItem, Book, db
from app.services.BookService import BookService
from datetime import datetime

class OrderService:
    
    @staticmethod
    def create_order_from_cart(user_id, shipping_data):
        """Create order from user's cart (checkout process)"""
        # Get cart items
        cart_items = CartItem.query.filter_by(user_id=user_id, is_deleted=False).all()
        
        if not cart_items:
            raise ValueError('Cart is empty')
        
        # Calculate total and validate stock
        total_amount = 0
        for cart_item in cart_items:
            book = Book.query.get(cart_item.book_id)
            if not book or book.is_deleted:
                raise ValueError(f'Book {cart_item.book_id} not found')
            
            if book.stock_quantity < cart_item.quantity:
                raise ValueError(f'Insufficient stock for {book.title}. Available: {book.stock_quantity}')
            
            total_amount += float(book.price) * cart_item.quantity
        
        # Create order
        order = OrderDetails(
            user_id=user_id,
            total_amount=total_amount,
            order_status='Pending',
            shipping_address=shipping_data.get('shipping_address', ''),
            city=shipping_data.get('city', ''),
            phone_number=shipping_data.get('phone_number', '')
        )
        db.session.add(order)
        db.session.flush()  # Get order ID
        
        # Create order items and reduce stock
        for cart_item in cart_items:
            book = Book.query.with_for_update().get(cart_item.book_id)
            
            # Reduce stock (with row lock to prevent race conditions)
            if book.stock_quantity < cart_item.quantity:
                db.session.rollback()
                raise ValueError(f'Stock changed for {book.title}')
            
            book.stock_quantity -= cart_item.quantity
            
            # Create order item
            order_item = OrderItem(
                order_details_id=order.id,
                book_id=cart_item.book_id,
                user_id=user_id,
                unit_price=book.price,
                quantity=cart_item.quantity
            )
            db.session.add(order_item)
            
            # Mark cart item as deleted
            cart_item.is_deleted = True
            cart_item.deleted_at = datetime.utcnow()
        
        db.session.commit()
        return order
    
    @staticmethod
    def get_user_orders(user_id):
        """Get all orders for a user"""
        return OrderDetails.query.filter_by(user_id=user_id, is_deleted=False).order_by(OrderDetails.created_at.desc()).all()
    
    @staticmethod
    def get_order_by_id(order_id, user_id=None):
        """Get order by ID (optionally filter by user)"""
        query = OrderDetails.query.filter_by(id=order_id, is_deleted=False)
        if user_id:
            query = query.filter_by(user_id=user_id)
        return query.first()
    
    @staticmethod
    def get_all_orders():
        """Get all orders (Admin only)"""
        return OrderDetails.query.filter_by(is_deleted=False).order_by(OrderDetails.created_at.desc()).all()
    
    @staticmethod
    def update_order_status(order_id, status):
        """Update order status (Admin only)"""
        valid_statuses = ['Pending', 'Confirmed', 'Shipped', 'Delivered', 'Cancelled']
        if status not in valid_statuses:
            raise ValueError(f'Invalid status. Must be one of: {", ".join(valid_statuses)}')
        
        order = OrderDetails.query.filter_by(id=order_id, is_deleted=False).first()
        if not order:
            return None
        
        order.order_status = status
        order.updated_at = datetime.utcnow()
        db.session.commit()
        return order
    
    @staticmethod
    def get_order_items(order_id):
        """Get all items in an order"""
        return OrderItem.query.filter_by(order_details_id=order_id, is_deleted=False).all()
