import pytest, cuid

# Nb. warnings generated by a bug: https://github.com/allure-framework/allure-python/issues/381

def pytest_configure():
    """
    Used to pass user parameters between tests
    """
    pytest.user_id = ""

@pytest.fixture
def password():
    return "test"

@pytest.fixture
def type():
    return "student"

@pytest.fixture(scope='session')
def email():
    id = cuid.CuidGenerator()
    return id.cuid() + "@live.rhul.ac.uk"

@pytest.fixture(scope='session')
def user_class():
    from ..libraries import user
    return user.user()

### TESTS ###

def test_create_student_user(user_class, email, password, type):
    """
    Test that a new student can be created.
    """

    name = "Joe Bloggs"

    pytest.user_id = user_class.create_user(name, email, password, type)

    assert pytest.user_id != False

def test_login_student_user_email(user_class, email, password):
    """ 
    Test that the new student can be logged in with email/password.
    """
    assert user_class.load_user(email=email) == True
    assert user_class.check_login(password) == True

def test_login_student_user_id(user_class, password):
    """
    Test that the new student can be logged in with user ID/password.
    """
    assert user_class.load_user(user_id=pytest.user_id) == True
    assert user_class.check_login(password) == True

def test_authentication_value(user_class, email, password):
    """
    Test that the user is always authenticated. 
    This relates to a flask_login bug. See issue #475.
    """
    assert user_class.is_authenticated == True

def test_load_user(user_class, email):
    """
    Test a user is loadable via email.
    """
    user_class.load_user(user_id=pytest.user_id)
    assert user_class.email == email

def test_invalid_load_user(user_class):
    """
    Test that a non-valid value does not cause a user to be loaded.
    """
    assert user_class.load_user("invalid_value") == False

def test_invalid_and_continued_load_user(user_class):
    """
    Test that a non-valid value does not cause a user to be loaded, 
    and attributes are False.
    """
    assert user_class.load_user(user_id="invalid_value") == False
    assert user_class.id == False

def test_ambiguous_load(user_class):
    """
    Test that providing multiple values in a load raises an exception.
    """
    with pytest.raises(Exception):
        user_class.load_user(user_id="value", email="value")

def test_premature_load_user(user_class):
    """
    Test that without load, user attributes are false.
    """
    assert user_class.id == False

def test_is_active(user_class, email):
    """
    Test that a user is marked as active.
    """
    assert user_class.load_user(email=email) == True
    assert user_class.is_active == True

def test_is_annon(user_class):
    """
    Test that a user is marked as anonymous.
    """
    assert user_class.is_anonymous == False

def test_user_id(user_class, email):
    """
    Test that the user ID attribute returns correctly.
    """
    assert user_class.load_user(email=email) == True
    assert user_class.id == pytest.user_id

def test_broken_user_id(user_class):
    """
    Test that an invalid email doesn't cause a user to be loaded.
    """
    assert user_class.load_user(email="adasd") == False
    assert user_class.id == False

def test_user_permissions(user_class, email, type):
    """
    Test that user permissions are returned.
    """
    assert user_class.load_user(email=email) == True
    assert user_class.get_permissions == type

def test_broken_user_permissions(user_class):
    """
    Test that for an invalid user load, no permissions are returned.
    """
    assert user_class.load_user(email="adasd") == False
    assert user_class.get_permissions == False