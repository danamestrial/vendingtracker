import pytest
from app import create_app
from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture
def app() -> Flask:
    """Create new app instance everytime for each test."""
    # Reads .env from backend/
    return create_app(env_path="../.env")


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """Create new test_client for the current instance."""
    return app.test_client()
