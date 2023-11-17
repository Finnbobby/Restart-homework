# pytest

from fastapi.testclient import TestClient
from .main import app
# Looks for files names with test_*.py
# $ pytest

# unittests
def test_basic_example():
    pass
    assert(True)

client = TestClient(app)

def test_put_api():
    response = client.put("/items/C3PO", json={
        "name": "Book1",
        "quantity": 10,
        "serial_number": "121323gma",
        "origin": {
            "country": "Ethiopia",
            "production_date": "25/06/23"
        }
    })  
    assert response.status_code == 200
    
