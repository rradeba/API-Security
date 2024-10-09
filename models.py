from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

dataBase = SQLAlchemy()


class Employee(dataBase.Model):
    __tablename__ = 'employees'
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    name = dataBase.Column(dataBase.String(100), nullable=False)
    position = dataBase.Column(dataBase.String(100), nullable=False)

class Product(dataBase.Model):
    __tablename__ = 'products'
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    name = dataBase.Column(dataBase.String(100), nullable=False)
    price = dataBase.Column(dataBase.Float, nullable=False)

class Order(dataBase.Model):
    __tablename__ = 'orders'
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    customer_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('customers.id'), nullable=False)
    product_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('products.id'), nullable=False)
    quantity = dataBase.Column(dataBase.Integer, nullable=False)
    total_price = dataBase.Column(dataBase.Float, nullable=False)

class Customer(dataBase.Model):
    __tablename__ = 'customers'
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    name = dataBase.Column(dataBase.String(100), nullable=False)
    email = dataBase.Column(dataBase.String(100), nullable=False)
    phone = dataBase.Column(dataBase.String(20), nullable=False)

class Production(dataBase.Model):
    __tablename__ = 'production'
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    product_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('products.id'), nullable=False)
    quantity_produced = dataBase.Column(dataBase.Integer, nullable=False)
    date_produced = dataBase.Column(dataBase.Date, nullable=False)


class User(dataBase.Model):
    __tablename__ = 'users'
    
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    username = dataBase.Column(dataBase.String(100), unique=True, nullable=False)
    password = dataBase.Column(dataBase.String(128), nullable=False)
    role = dataBase.Column(dataBase.String(50), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)