from app.models import Category, db
from datetime import datetime

class CategoryService:
    
    @staticmethod
    def get_all_categories():
        """Get all active categories"""
        return Category.query.filter_by(is_deleted=False).all()
    
    @staticmethod
    def get_category_by_id(category_id):
        """Get category by ID"""
        return Category.query.filter_by(id=category_id, is_deleted=False).first()
    
    @staticmethod
    def create_category(data):
        """Create new category"""
        new_category = Category(
            category_type=data['category_type'],
            created_by=data.get('created_by', '')
        )
        db.session.add(new_category)
        db.session.commit()
        return new_category
    
    @staticmethod
    def update_category(category_id, data):
        """Update existing category"""
        category = Category.query.filter_by(id=category_id, is_deleted=False).first()
        if not category:
            return None
        
        category.category_type = data.get('category_type', category.category_type)
        category.updated_at = datetime.utcnow()
        db.session.commit()
        return category
    
    @staticmethod
    def delete_category(category_id):
        """Soft delete category"""
        category = Category.query.filter_by(id=category_id, is_deleted=False).first()
        if not category:
            return False
        
        category.is_deleted = True
        category.deleted_at = datetime.utcnow()
        db.session.commit()
        return True
