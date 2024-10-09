from functools import wraps
from flask import request, jsonify
from .utils import decode_token

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization')
            user_id = decode_token(token)
            if user_id is None:
                return jsonify({'message': 'Access denied'}), 403
            user = User.query.get(user_id)  
            if user.role != role:
                return jsonify({'message': 'Access denied'}), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator
