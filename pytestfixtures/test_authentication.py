#Assignment 4: Authentication Fixture
#Create a fixture returning username, token, and role. Write tests that verify the token exists, the user is
#authenticated, and the role is admin

import pytest


@pytest.fixture
def authentication():
    return {
        "username": "devika",
        "token": "abc123token",
        "role": "admin"
    }

def test_token_exists(authentication):
    assert "token" in authentication    #verifing token exists
    assert authentication["role"] != "" #verifying token is not empty
    assert authentication["token"]== "abc123token" #verifying token with actual value


def test_user_authenticated(authentication):
    assert authentication["username"] == "devika"
    

def test_role_admin(authentication):
    
    assert authentication["role"] == "admin"