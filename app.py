from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from config import Config
from controllers.auth import auth_bp
from controllers.employees import employees_bp
from controllers.products import products_bp
from controllers.orders import orders_bp
from controllers.customers import customers_bp
from controllers.production import production_bp

db = SQLAlchemy()
limiter = Limiter()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    limiter.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(employees_bp, url_prefix='/employees')
    app.register_blueprint(products_bp, url_prefix='/products')
    app.register_blueprint(orders_bp, url_prefix='/orders')
    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(production_bp, url_prefix='/production')

    with app.app_context():
        db.create_all() 

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
