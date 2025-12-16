from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from config.development import DevelopmentConfig
from app.models import db

jwt = JWTManager()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    # Register blueprints with API versioning
    from app.routes.itemRoutes import items_bp
    from app.routes.UserRoutes import users_bp
    from app.routes.AuthRoutes import auth_bp
    from app.routes.AuthorRoutes import author_bp
    from app.routes.CategoryRoutes import category_bp
    from app.routes.BookRoutes import book_bp
    from app.routes.CartRoutes import cart_bp
    from app.routes.CartHistoryRoutes import cart_history_bp
    from app.routes.OrderRoutes import order_bp
    from app.routes.ReviewRoutes import review_bp
    
    # API v1 routes
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(users_bp, url_prefix='/api/v1')
    app.register_blueprint(author_bp, url_prefix='/api/v1')
    app.register_blueprint(category_bp, url_prefix='/api/v1')
    app.register_blueprint(book_bp, url_prefix='/api/v1')
    app.register_blueprint(cart_bp, url_prefix='/api/v1')
    app.register_blueprint(cart_history_bp, url_prefix='/api/v1/cart-history')
    app.register_blueprint(order_bp, url_prefix='/api/v1')
    app.register_blueprint(review_bp, url_prefix='/api/v1/reviews')
    
    # Legacy routes (keep for backward compatibility)
    app.register_blueprint(items_bp, url_prefix='/api')
    
    @app.route('/')
    def home():
        return {"message": "Welcome to Flask API"}
    
    return app
