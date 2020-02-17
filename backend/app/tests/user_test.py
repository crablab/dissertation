import pytest, cuid

def pytest_configure():
    """
    Used to pass user ID bewteen tests once a user is created
    """

    pytest.user_id = ""

@pytest.fixture(scope='session')
def email():
    id = cuid.CuidGenerator()
    return id.cuid() + "@live.rhul.ac.uk"

@pytest.fixture(scope='session')
def user_class():
    from ..libraries import user
    return user.user()

def test_create_student_user(user_class, email):
    name = "Joe Bloggs"
    password = "test"
    type = "student"

    pytest.user_id = user_class.create_user(name, email, password, type)

    assert pytest.user_id != False

def test_login_student_user(user_class, email):
    password = "test"

    assert user_class.check_login(email, password) == True

def test_premature_load_user(user_class):
    assert user_class.get_user() == False

def test_load_user(user_class, email):
    user_class.load_user(pytest.user_id)
    assert user_class.get_user()['email'] == email

def test_invalid_load_user(user_class):
    assert user_class.load_user("invalid_value") == False

def test_invalid_and_continued_load_user(user_class):
    assert user_class.load_user("invalid_value") == False
    assert user_class.get_user() == False