# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello from FastAPI with Jenkins & SonarQube!"}

def test_average_success():
    resp = client.get("/average?numbers=10&numbers=20&numbers=30")
    assert resp.status_code == 200
    assert resp.json()["average"] == 20.0

def test_average_missing_query():
    resp = client.get("/average")
    assert resp.status_code == 422  # missing required query param

def test_reverse_string():
    resp = client.get("/reverse?text=SonarQube")
    assert resp.status_code == 200
    assert resp.json()["reversed"] == "ebuQranoS"
