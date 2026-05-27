from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}