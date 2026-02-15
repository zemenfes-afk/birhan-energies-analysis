import pytest
import sys
import os

# Add backend directory to path so we can import app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_api_online(client):
    """Test 1: Verify API root is online."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'online'

def test_get_prices(client):
    """Test 2: Verify prices endpoint returns a list."""
    response = client.get('/api/prices')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0

def test_get_events(client):
    """Test 3: Verify events endpoint returns data."""
    response = client.get('/api/events')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_summary_metrics(client):
    """Test 4: Verify summary contains correct financial keys."""
    response = client.get('/api/analysis-summary')
    assert response.status_code == 200
    data = response.json
    assert 'average_price' in data
    assert 'max_price' in data
    assert data['total_days'] > 0

def test_404_route(client):
    """Test 5: Verify handling of non-existent routes."""
    response = client.get('/api/unknown')
    assert response.status_code == 404