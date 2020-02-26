import pytest, cuid

@pytest.fixture(scope='session')
def users_class():
    from ..libraries import users
    return users.users()

def test_users_load(users_class):
    assert users_class.load_users() == True

def test_users_returns(users_class):
    assert users_class.load_users() == True
    list = user_class.get_users()

    assert list.count() > 0