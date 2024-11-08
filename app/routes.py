from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from app import mongo
from app.models import UserSchema
from app.utils import hash_password, check_password

user_bp = Blueprint('user_bp', __name__)
user_schema = UserSchema()
users_collection = mongo.db.users

@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = list(users_collection.find())
    for user in users:
        user['id'] = str(user['_id'])
        del user['_id']
    return jsonify(users), 200

@user_bp.route('/<id>', methods=['GET'])
def get_user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if user:
        user['id'] = str(user['_id'])
        del user['_id']
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    data['password'] = hash_password(data['password'])
    result = users_collection.insert_one(data)
    return jsonify({'id': str(result.inserted_id)}), 201

@user_bp.route('/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    if 'password' in data:
        data['password'] = hash_password(data['password'])
    users_collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'User updated'}), 200

@user_bp.route('/<id>', methods=['DELETE'])
def delete_user(id):
    users_collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'User deleted'}), 200
