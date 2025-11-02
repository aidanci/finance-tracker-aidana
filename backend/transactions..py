from flask import Blueprint, request, jsonify
from .auth import token_required
from .database import get_conn
import datetime

bp = Blueprint("transactions", __name__, url_prefix="/transactions")

@bp.post("/")
@token_required
def add_transaction():
    data = request.get_json() or {}
    title = data.get("title")
    category = data.get("category")
    type_ = data.get("type")  # "income" or "expense"
    amount = data.get("amount")
    date = data.get("date")

    if not all([title, category, type_, amount, date]):
        return jsonify({"error": "All fields are required"}), 400
    if type_ not in ("income", "expense"):
        return jsonify({"error": "Type must be 'income' or 'expense'"}), 400
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        return jsonify({"error": "Amount must be a positive number"}), 400

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO transactions (title, category, type, amount, date)
        VALUES (?, ?, ?, ?, ?)
        """,
        (title, category, type_, amount, date),
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Transaction added"}), 201


@bp.get("/")
@token_required
def list_transactions():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, category, type, amount, date FROM transactions ORDER BY date DESC"
    )
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify(rows), 200


@bp.get("/<int:transaction_id>")
@token_required
def get_transaction(transaction_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, category, type, amount, date FROM transactions WHERE id=?",
        (transaction_id,),
    )
    row = cur.fetchone()
    conn.close()
    if not row:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify(dict(row)), 200


@bp.put("/<int:transaction_id>")
@token_required
def update_transaction(transaction_id):
    data = request.get_json() or {}
    title = data.get("title")
    category = data.get("category")
    type_ = data.get("type")
    amount = data.get("amount")
    date = data.get("date")

    if not all([title, category, type_, amount, date]):
        return jsonify({"error": "All fields are required"}), 400

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE transactions
        SET title=?, category=?, type=?, amount=?, date=?, updated_at=CURRENT_TIMESTAMP
        WHERE id=?
        """,
        (title, category, type_, amount, date, transaction_id),
    )
    conn.commit()
    updated = cur.rowcount
    conn.close()
    if updated == 0:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify({"message": "Transaction updated"}), 200


@bp.delete("/<int:transaction_id>")
@token_required
def delete_transaction(transaction_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
    conn.commit()
    deleted = cur.rowcount
    conn.close()
    if deleted == 0:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify({"message": "Transaction deleted"}), 200