from app.models import User, db
from app import bcrypt
from datetime import datetime, timezone

class UserService:
    
    @staticmethod
    def get_all_users():
        return User.query.filter_by(deleted_at=None).all()
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.filter_by(id=user_id, deleted_at=None).first()
    
    @staticmethod
    def create_user(data):
        # Hash password before storing
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        
        new_user = User(
            username=data['username'],
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            role=data.get('role', 0),
            phone_number=data.get('phone_number'),
            address=data.get('address'),
            city=data.get('city'),
            province=data.get('province'),
            date_of_birth=data.get('date_of_birth')
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def update_user(user_id, data):
        user = User.query.filter_by(id=user_id, deleted_at=None).first()
        if not user:
            return None
        
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.phone_number = data.get('phone_number', user.phone_number)
        user.address = data.get('address', user.address)
        user.city = data.get('city', user.city)
        user.province = data.get('province', user.province)
        
        db.session.commit()
        return user
    
    @staticmethod
    def delete_user(user_id):
        user = User.query.filter_by(id=user_id, deleted_at=None).first()
        if not user:
            return False
        
        user.deleted_at = datetime.now(timezone.utc)
        db.session.commit()
        return True
