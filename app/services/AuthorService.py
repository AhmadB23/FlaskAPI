from app.models import Author, db
from datetime import datetime

class AuthorService:
    
    @staticmethod
    def get_all_authors():
        """Get all active authors"""
        return Author.query.filter_by(is_deleted=False).all()
    
    @staticmethod
    def get_author_by_id(author_id):
        """Get author by ID"""
        return Author.query.filter_by(id=author_id, is_deleted=False).first()
    
    @staticmethod
    def create_author(data):
        """Create new author"""
        new_author = Author(
            author_name=data['author_name'],
            created_by=data.get('created_by', '')
        )
        db.session.add(new_author)
        db.session.commit()
        return new_author
    
    @staticmethod
    def update_author(author_id, data):
        """Update existing author"""
        author = Author.query.filter_by(id=author_id, is_deleted=False).first()
        if not author:
            return None
        
        author.author_name = data.get('author_name', author.author_name)
        author.updated_at = datetime.utcnow()
        db.session.commit()
        return author
    
    @staticmethod
    def delete_author(author_id):
        """Soft delete author"""
        author = Author.query.filter_by(id=author_id, is_deleted=False).first()
        if not author:
            return False
        
        author.is_deleted = True
        author.deleted_at = datetime.utcnow()
        db.session.commit()
        return True
