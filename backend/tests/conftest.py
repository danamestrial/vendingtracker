import os

import pytest

from app import create_app


@pytest.fixture
def app():
    """Creating new app instance everytime for each test"""
    # Reads .env from backend/
    return create_app(env_path='../.env')


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
