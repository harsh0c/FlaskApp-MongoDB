from flask import Flask,jsonify
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)

    @app.route('/', methods=['GET'])
    def home():
        return jsonify({'message': 'Welcome to the User Management API'}), 200

    with app.app_context():
        from app.routes import user_bp
        app.register_blueprint(user_bp, url_prefix='/users')

    return app
