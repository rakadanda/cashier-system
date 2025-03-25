from flask import Flask
from flask_migrate import Migrate
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret_key'
    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    from .routes.auth import bp as auth_bp
    from .routes.products import bp as products_bp
    from .routes.transactions import bp as transactions_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(transactions_bp)
    
    return app
