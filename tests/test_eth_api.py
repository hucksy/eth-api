from fastapi.testclient import TestClient
from app.main import app

tc = TestClient(app)


def test_root():
    response = tc.get("/")
    assert response.json() == {'message': 'hulloh beautiful world!'}
    assert response.status_code == 200

