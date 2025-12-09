from flask import Blueprint, jsonify, request
from app.models import User, db
from app.services.UserService import UserService

users_bp = Blueprint('users', __name__)

@users_bp.route("/users", methods=['POST'])
def create_user():
    data = request.get_json()
    users =  UserService.create_users(data)
