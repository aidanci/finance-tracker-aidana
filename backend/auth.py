from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from sqlite3 import IntegrityError
import jwt, datetime, os
from functools import wraps
from .database import get_conn

bp = Blueprint("auth", __name__, url_prefix="/auth")

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Missing token"}), 401
        try:
            token = token.split(" ")[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            conn = get_conn()
            user = conn.execute(
                "SELECT id, login, role FROM users WHERE id=?", (data["id"],)
            ).fetchone()
            conn.close()
            if not user:
                return jsonify({"error": "User not found"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except Exception:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated


@bp.post("/register")
def register():
    data = request.get_json() or {}
    login = data.get("login")
    password = data.get("password")

    if not login or not password:
        return jsonify({"error": "Missing login or password"}), 400
    if len(password) < 5:
        return jsonify({"error": "Password too short"}), 400

    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (login, password_hash, role) VALUES (?, ?, ?)",
            (login, generate_password_hash(password), "USER")
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "User registered"}), 201
    except IntegrityError:
        conn.close()
        return jsonify({"error": "Login already exists"}), 400


@bp.post("/login")
def login():
    data = request.get_json() or {}
    login = data.get("login")
    password = data.get("password")

    if not login or not password:
        return jsonify({"error": "Missing login or password"}), 400

    conn = get_conn()
    user = conn.execute(
        "SELECT id, password_hash, role FROM users WHERE login=?", (login,)
    ).fetchone()
    conn.close()

    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = jwt.encode({
        "id": user["id"],
        "role": user["role"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, SECRET_KEY, algorithm="HS256")

    return jsonify({"token": token})