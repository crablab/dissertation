import pytest

@pytest.fixture
def dbHandler():
    from db import database
    return database()

def test_connection(dbHandler):
    assert (dbHandler.check_connection() != None)
