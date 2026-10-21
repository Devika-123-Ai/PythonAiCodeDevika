# Assignment 5: Temporary File Fixture
# Create a fixture that creates a temporary file, writes test data, yields the file path/content to the test, and
# removes or closes resources during teardown.

import pytest


@pytest.fixture

def temp_file():
    filename = "testfile.txt"
    file = open(filename, "w")
    file.write("This is test data")
    file.close()

    yield filename

    print("Taskcompleted")


def test_temp_file(temp_file):
    file = open(temp_file, "r")
    content = file.read()
    file.close()

    assert content == "This is test data"