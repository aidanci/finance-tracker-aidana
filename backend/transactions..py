from flask import Blueprint, jsonify, request
from sqlite3 import IntegrityError
from .database import get_conn
from .auth import token_required
from .validators import validate_transaction

bp = Blueprint("transactions", __name__, url_prefix="/transactions")

@bp.get("/")
@token_required
def list_transactions():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM transactions ORDER BY date DESC").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@bp.post("/")
@token_required
def create_transaction():
    data = request.get_json(silent=True) or {}
    error = validate_transaction(data)
    if error:
        return jsonify({"error": error}), 400

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO transactions (title, category, type, amount, date)
        VALUES (?, ?, ?, ?, ?)
    """, (data["title"], data["category"], data["type"], data["amount"], data["date"]))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return jsonify({"message": "Transaction added", "id": new_id}), 201

@bp.delete("/<int:tid>")
@token_required
def delete_transaction(tid: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM transactions WHERE id=?", (tid,))
    conn.commit()
    deleted = cur.rowcount
    conn.close()
    if deleted == 0:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify({"message": "Transaction deleted"})