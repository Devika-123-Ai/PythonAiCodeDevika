#Assignment 2: Database Connection Fixture
#Create a fixture that prints 'Connecting to database', yields a fake database connection, and prints
#'Closing database' after the test. Demonstrate setup and teardown.

import pytest

@pytest.fixture
def dbconnection():
    print("Connecting to database")     #this one is setup

    db= "fake database connection"

    yield db

    print("Closing database")       #yield pauses the test func ,after test execution its cleanup/teardown


def test_database(dbconnection):
    print("message:", dbconnection)