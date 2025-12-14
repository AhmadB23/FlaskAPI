from flask import Blueprint, jsonify, request
from app.models import User, db
from app.services.UserService import UserService

users_bp = Blueprint('users', __name__)

# GET all users
@users_bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

# GET user by ID
@users_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

# POST create user
@users_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user = UserService.create_user(data)
        return jsonify(user.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# PUT update user
@users_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.get_json()
        user = UserService.update_user(user_id, data)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# DELETE user
@users_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = UserService.delete_user(user_id)
    if not success:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User deleted successfully'}), 200
