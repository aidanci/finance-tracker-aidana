import pytest
from backend.app import create_app
from backend.database import get_conn, init_db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()
    yield client

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200

def test_register_and_login(client):
    r = client.post("/auth/register", json={"login": "user1", "password": "12345"})
    assert r.status_code in (201, 400)
    r = client.post("/auth/login", json={"login": "user1", "password": "12345"})
    assert r.status_code == 200
    assert "token" in r.get_json()