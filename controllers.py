from flask import Blueprint, jsonify, request
from .models import Employee, Product, Order, Customer, Production
from . import dataBase, limiter
from .utils import encode_token

main_blueprint = Blueprint('main', __name__)

# Employee routes
@limiter.limit("10 per minute")
@main_blueprint.route('/employees', methods=['GET', 'POST'])
def manage_employees():
    if request.method == 'GET':
        employees = Employee.query.all()
        return jsonify([{'id': emp.id, 'name': emp.name, 'position': emp.position} for emp in employees])
    
    if request.method == 'POST':
        data = request.get_json()
        new_employee = Employee(name=data['name'], position=data['position'])
        dataBase.session.add(new_employee)
        dataBase.session.commit()
        return jsonify({'message': 'Employee added'}), 201

# Product routes
@limiter.limit("10 per minute")
@main_blueprint.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == 'GET':
        products = Product.query.all()
        return jsonify([{'id': prod.id, 'name': prod.name, 'price': prod.price} for prod in products])
    
    if request.method == 'POST':
        data = request.get_json()
        new_product = Product(name=data['name'], price=data['price'])
        dataBase.session.add(new_product)
        dataBase.session.commit()
        return jsonify({'message': 'Product added'}), 201

# Order routes
@limiter.limit("10 per minute")
@main_blueprint.route('/orders', methods=['GET', 'POST'])
def manage_orders():
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        orders = Order.query.paginate(page=page, per_page=per_page, error_out=False)
        return jsonify({
            'orders': [{'id': ord.id, 'customer_id': ord.customer_id, 'product_id': ord.product_id, 'quantity': ord.quantity, 'total_price': ord.total_price} for ord in orders.items],
            'total': orders.total,
            'pages': orders.pages,
            'current_page': orders.page
        })
    
    if request.method == 'POST':
        data = request.get_json()
        new_order = Order(customer_id=data['customer_id'], product_id=data['product_id'], quantity=data['quantity'], total_price=data['total_price'])
        dataBase.session.add(new_order)
        dataBase.session.commit()
        return jsonify({'message': 'Order added'}), 201

# Customer routes
@limiter.limit("10 per minute")
@main_blueprint.route('/customers', methods=['GET', 'POST'])
def manage_customers():
    if request.method == 'GET':
        customers = Customer.query.all()
        return jsonify([{'id': cust.id, 'name': cust.name, 'email': cust.email, 'phone': cust.phone} for cust in customers])
    
    if request.method == 'POST':
        data = request.get_json()
        new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
        dataBase.session.add(new_customer)
        dataBase.session.commit()
        return jsonify({'message': 'Customer added'}), 201

# Production routes
@limiter.limit("10 per minute")
@main_blueprint.route('/production', methods=['GET', 'POST'])
def manage_production():
    if request.method == 'GET':
        production = Production.query.all()
        return jsonify([{'id': prod.id, 'product_id': prod.product_id, 'quantity_produced': prod.quantity_produced, 'date_produced': prod.date_produced.isoformat()} for prod in production])
    
    if request.method == 'POST':
        data = request.get_json()
        new_production = Production(product_id=data['product_id'], quantity_produced=data['quantity_produced'], date_produced=data['date_produced'])
        dataBase.session.add(new_production)
        dataBase.session.commit()
        return jsonify({'message': 'Production record added'}), 201


@main_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        token = encode_token(user.id)
        return jsonify({'token': token, 'message': 'Login successful'}), 200
    
    return jsonify({'message': 'Invalid username or password'}), 401



@app.route('/admin/data', methods=['POST'])
@role_required('admin')
def create_admin_data():
    return jsonify({'message': 'Admin data created'}), 201

@app.route('/user/data', methods=['POST'])
@role_required('user')
def create_user_data():
    return jsonify({'message': 'User data created'}), 201
