from app.main import app
from app.eth_api.models import Base
from app.database import get_db
from fastapi.testclient import TestClient
from app.config import get_env_configs
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest


test_engine = create_engine(get_env_configs().DATABASE_URL_TEST)
TestSession = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture
def test_session():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    db = TestSession()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def test_client(test_session):
    def override_get_db():
        try:
            yield test_session
        finally:
            test_session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


def test_root(test_client):
    response = test_client.get("/")
    assert response.json() == {'message': 'hulloh beautiful world!'}
    assert response.status_code == 200


@pytest.mark.parametrize("block_num", [15883669])
def test_get_block(test_client, block_num):
    response = test_client.get(f"/eth/get_block/{block_num}")
    assert response.status_code == 200
    assert block_num == response.json().get('number')


@pytest.mark.parametrize("block_num", [15883669])
def test_add_block(test_client, block_num):
    response = test_client.post(f"/eth/add_block/{block_num}")
    assert response.status_code == 201
    assert block_num == response.json().get('number')
