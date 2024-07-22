"""
Test module for lab 6
"""
import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True

    yield app.test_client()

def test_racing(client):
    response = client.get("/sim_racing")
    assert 200 == response.status_code
    assert b"IMSA" in response.data

def test_main(client):
    response = client.get("/")
    assert 200 == response.status_code
    assert b"George Rowland" in response.data

def test_games(client):
    response = client.get("/games")
    assert 200 == response.status_code
    assert b"<title>Games</title>" in response.data
    assert b"Annihilation" in response.data

def test_bad(client):
    response = client.get("/asdf")
    assert 404 == response.status_code
    assert b"I'm sorry the webpage you requested is in another castle." in response.data
