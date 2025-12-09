from flask import Flask
from config.development import DevelopmentConfig
from app.models import db

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    from app.routes.items import items_bp
    app.register_blueprint(items_bp, url_prefix='/api')
    
    @app.route('/')
    def home():
        return {"message": "Welcome to Flask API"}
    
    return app
