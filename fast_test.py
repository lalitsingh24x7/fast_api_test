from fastapi.testclient import TestClient
from main import app, show

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_show():
    assert show(1, 2) == 3
