# Assignment 6: API Client Fixture
# Create a fake APIClient with get(), post(), and delete(). Create a reusable api_client fixture and write
# separate tests for each operation.
import pytest

class APIClient:

    def get(self):
        return "GET successful"

    def post(self):
        return "POST successful"

    def delete(self):
        return "DELETE successful"

@pytest.fixture

def api_client():
    return APIClient()      #reusable api client fixture


def test_get(api_client):
    assert api_client.get() == "GET successful"
def test_post(api_client):
    assert api_client.post() == "POST successful"
def test_delete(api_client):
    assert api_client.delete() == "DELETE successful"