from fastapi.testclient import TestClient
from app.main import app
import io

# Create a TestClient instance using the FastAPI app defined in app/main.py. This client will be used to send requests to the endpoints for testing purposes.
client = TestClient(app)

# Test the /health endpoint to ensure it returns the expected status code and response content.
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
