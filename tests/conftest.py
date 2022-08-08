import pytest

from zyambo.app import app
from werkzeug.test import Client

@pytest.fixture()
def client():
    return app.test_client()