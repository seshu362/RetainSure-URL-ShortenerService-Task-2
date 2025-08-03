import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json.get("status") == "URL Shortener Service running"

def test_shorten_url_valid(client):
    resp = client.post("/api/shorten", json={"url": "https://example.com"})
    assert resp.status_code == 201
    data = resp.json
    assert "short_code" in data
    assert "short_url" in data

def test_shorten_url_missing(client):
    resp = client.post("/api/shorten", json={})
    assert resp.status_code == 400
    assert "error" in resp.json

def test_shorten_url_invalid(client):
    resp = client.post("/api/shorten", json={"url": "not-a-valid-url"})
    assert resp.status_code == 400
    assert "error" in resp.json

def test_redirect_and_stats(client):
    # Shorten URL
    resp = client.post("/api/shorten", json={"url": "https://example.com"})
    code = resp.json["short_code"]
    
    # Redirect (should be 302)
    redirect_resp = client.get(f"/{code}")
    assert redirect_resp.status_code == 302
    assert redirect_resp.location == "https://example.com"
    
    # Stats
    stats_resp = client.get(f"/api/stats/{code}")
    assert stats_resp.status_code == 200
    stats = stats_resp.json
    assert stats["url"] == "https://example.com"
    assert stats["clicks"] == 1

def test_stats_not_found(client):
    resp = client.get("/api/stats/notexist")
    assert resp.status_code == 404
    assert "error" in resp.json

def test_redirect_not_found(client):
    resp = client.get("/notexist")
    assert resp.status_code == 404
    assert "error" in resp.json
