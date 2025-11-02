from flask import request, jsonify
from flask_jwt_extended import jwt_required
from . import bp
from .model import get_all, get_by_id, create, update, delete, create_table

create_table()

@bp.route("/", methods=["GET"])
@jwt_required()
def list_transactions():
    return jsonify(get_all())


@bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_transaction(id):
    item = get_by_id(id)
    if not item:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify(item)


@bp.route("/", methods=["POST"])
@jwt_required()
def add_transaction():
    data = request.get_json()
    required = ["title", "category", "type", "amount", "date"]
    if not all(field in data for field in required):
        return jsonify({"error": "Missing fields"}), 400
    try:
        create(data)
        return jsonify({"message": "Transaction added"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def edit_transaction(id):
    if not get_by_id(id):
        return jsonify({"error": "Transaction not found"}), 404
    data = request.get_json()
    try:
        update(id, data)
        return jsonify({"message": "Transaction updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_transaction(id):
    if not get_by_id(id):
        return jsonify({"error": "Transaction not found"}), 404
    delete(id)
    return jsonify({"message": "Transaction deleted"}), 200