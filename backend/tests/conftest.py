import os
import sys
import pytest
from fastapi.testclient import TestClient

# ضبط مسار العمل للـ Root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client