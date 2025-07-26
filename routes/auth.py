from flask import Blueprint, request, jsonify
from services.db import users_col

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    try:
        if users_col.find_one({"username": data["username"]}):
            return jsonify({"error": "Username already exists"}), 400
        users_col.insert_one({"username": data["username"], "password": data["password"]})
        return jsonify({"message": "User created"})
    except Exception as e:
        return jsonify({"error": "Signup failed", "details": str(e)}), 500

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    try:
        user = users_col.find_one({"username": data["username"], "password": data["password"]})
        if user:
            return jsonify({"message": "Login successful"})
        return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": "Login failed", "details": str(e)}), 500