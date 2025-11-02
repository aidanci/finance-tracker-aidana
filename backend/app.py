from flask import Flask, send_from_directory
from flask_cors import CORS
from pathlib import Path
from werkzeug.security import generate_password_hash
from .database import init_db, get_conn
from .transactions import bp as transactions_bp 
from .auth import bp as auth_bp


def create_app():
    app = Flask(__name__, static_folder="../frontend", static_url_path="")
    CORS(app)

    init_db()

    conn = get_conn()
    conn.execute(
        "INSERT OR IGNORE INTO users (login, password_hash, role) VALUES (?, ?, ?)",
        ("testuser", generate_password_hash("12345"), "USER")
    )
    conn.commit()
    conn.close()

    app.register_blueprint(transactions_bp)
    app.register_blueprint(auth_bp)

    @app.route("/")
    def index():
        frontend_path = Path(app.static_folder) / "index.html"
        if not frontend_path.exists():
            return "<h3>⚠️ index.html not found — check frontend folder</h3>", 404
        return send_from_directory(app.static_folder, "index.html")

    @app.route("/opis")
    def opis():
        """Public info page (no login required)."""
        return send_from_directory(app.static_folder, "about.html")

    @app.route("/<path:path>")
    def static_proxy(path):
        """Serve static files from frontend folder"""
        return send_from_directory(app.static_folder, path)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)