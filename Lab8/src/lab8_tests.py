"""
Test module for lab 6
"""
import pytest
from app import create_app
import backend

@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    users = backend.Users()

    yield app.test_client()

def test_unlogged_racing(client):
    response = client.get("/sim_racing")
    assert 302 == response.status_code

def test_unlogged_main(client):
    response = client.get("/loggedin")
    assert 302 == response.status_code

def test_unlogged_games(client):
    response = client.get("/games")
    assert 302 == response.status_code

def test_bad(client):
    response = client.get("/asdf")
    assert 404 == response.status_code
    assert b"I'm sorry the webpage you requested is in another castle." in response.data

def test_base(client):
    response = client.get("/")
    assert 302 == response.status_code

def test_login(client):
    response = client.get("/login")
    assert 200 == response.status_code
    response = client.post('/login', data={'uname': 'test',
                                           'pword': 'Hello'}, follow_redirects=True)
    assert 200 == response.status_code
    assert b"George" in response.data

def test_login_fail(client):
    response = client.get("/login")
    assert 200 == response.status_code
    response = client.post('/login', data={'uname': 'test',
                                           'pword': 'jello'}, follow_redirects=True)
    assert 200 == response.status_code
    assert b"Try again or sign up" in response.data

def get_logged_in_client(client):
    response = client.get("/login")
    response = client.post('/login', data={'uname': 'test',
                                           'pword': 'Hello'}, follow_redirects=True)
    return client

def test_loggedin(client):
    client = get_logged_in_client(client)
    response = client.get('/loggedin')
    assert 200 == response.status_code
    assert b'George Rowland' in response.data

def test_games(client):
    client = get_logged_in_client(client)
    response = client.get('/games')
    assert 200 == response.status_code
    assert b'Games' in response.data
    assert b'Astro Traveler' in response.data

def test_racing(client):
    client = get_logged_in_client(client)
    response = client.get('/sim_racing')
    assert 200 == response.status_code
    assert b'My Cars' in response.data
    assert b'Sim Racing' in response.data

def test_login():
    u = backend.Users()
    assert u.login("bob", "!@#123QWEqwe") == True

def test_login_invalid():
    u = backend.Users()
    assert u.login("bob", "!@#123QWE") == False

def test_user_exists():
    u = backend.Users()
    assert u.user_exist("bob") == True

def test_user_not_exist():
    u = backend.Users()
    assert u.user_exist("chuck") == False

def test_password_short():
    p = backend.Password("Password!12")
    assert p.has_upper() is True
    assert p.has_lower() is True
    assert p.has_digit() is True
    assert p.has_special() is True
    assert p.valid_password() is False

def test_password_no_upper():
    p = backend.Password("1234asdf!")
    assert p.has_upper() is False
    assert p.has_lower() is True
    assert p.has_digit() is True
    assert p.has_special() is True
    assert p.valid_password() is False

def test_password_no_lower():
    p = backend.Password("1234ASD!")
    assert p.has_upper() is True
    assert p.has_lower() is False
    assert p.has_digit() is True
    assert p.has_special() is True
    assert p.valid_password() is False

def test_password_no_special():
    p = backend.Password("1234ASDasdfre")
    assert p.has_upper() is True
    assert p.has_lower() is True
    assert p.has_digit() is True
    assert p.has_special() is False
    assert p.valid_password() is False

def test_password_good():
    p = backend.Password("1234ASDasdfre!@#$")
    assert p.has_upper() is True
    assert p.has_lower() is True
    assert p.has_digit() is True
    assert p.has_special() is True
    assert p.valid_password() is True

