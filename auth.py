import jwt
import datetime
from functools import wraps
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

SECRET_KEY = "CHANGE_ME_SUPER_SECRET"

# Simple in-memory users store (upgrade later to PostgreSQL)
USERS = {}

def create_token(username):
    payload = {
        "user": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token missing"}), 401
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except Exception:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated


def register_user(username, password):
    if username in USERS:
        return False
    USERS[username] = generate_password_hash(password)
    return True

def authenticate_user(username, password):
    if username not in USERS:
        return False
    return check_password_hash(USERS[username], password)