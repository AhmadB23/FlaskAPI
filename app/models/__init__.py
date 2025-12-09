from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models
from app.models.Users import User

__all__ = ['db', 'User']
