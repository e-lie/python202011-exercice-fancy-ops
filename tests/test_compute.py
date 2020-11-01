import os
import tempfile
import pytest

from web_app import web_app

@pytest.fixture
def client():
    with web_app.test_client() as client:
        yield client

def test_compute_add_5_5(client):
    return_value = client.get('/add/5/5')
    assert b'5 + 5 = 10' in return_value.data

def test_compute_add_0_0(client):
    return_value = client.get('/add/0/0')
    assert b'0 + 0 = 0' in return_value.data
