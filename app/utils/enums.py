from flask_jwt_extended import get_jwt_identity
from app.models import User

class Enums:
    class UserRole:
        isADMIN = 1
        isUSER = 2
        isGUEST = 3

def is_admin():
    """Check if current user is admin (role >= 1)"""
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return user and user.role >= 1


