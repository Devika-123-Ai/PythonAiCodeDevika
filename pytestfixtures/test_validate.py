#Assignment 1: Basic User Fixture
#Create a pytest fixture named user that returns username, email, and role. Write three tests using the
#same fixture to validate username, email, and role.


import pytest

@pytest.fixture
def user():
    return   { "username":"Devika",
             "email":"devika@gmail.com",
             "role":"admin"
             }

def test_username(user):
    print(user["username"])
def test_email(user):
    print(user["email"])
def test_role(user):
    print(user["role"])     # 3 testcases with testdata