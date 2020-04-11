import pytest, cuid

@pytest.fixture(scope='session')
def users_class():
    from ..libraries import users
    return users.users()

def test_users_load(users_class):
    """
    Tests that the `users` class can be loaded. 
    """
    assert users_class.load_users() == True

def test_users_returns(users_class):
    """
    Tests that the users class returns results and a list greater than 0. 
    """
    assert users_class.load_users() == True
    list = users_class.users

    assert list != False
    assert len(list) > 0