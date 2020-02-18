import pytest, cuid

def pytest_configure():
    """
    Used to pass user parameters between tests
    """
    pytest.user_id = ""

@pytest.fixture
def password():
    return "test"

@pytest.fixture(scope='session')
def email():
    id = cuid.CuidGenerator()
    return id.cuid() + "@live.rhul.ac.uk"

@pytest.fixture(scope='session')
def user_class():
    from ..libraries import user
    return user.user()

def test_create_student_user(user_class, email, password):
    name = "Joe Bloggs"
    type = "student"

    pytest.user_id = user_class.create_user(name, email, password, type)

    assert pytest.user_id != False

def test_login_student_user_email(user_class, email, password):
    assert user_class.load_user(email=email) == True
    assert user_class.check_login(password) == True

def test_login_student_user_id(user_class,password):
    assert user_class.load_user(user_id=pytest.user_id) == True
    assert user_class.check_login(password) == True

def test_load_user(user_class, email):
    user_class.load_user(user_id=pytest.user_id)
    assert user_class.get_user()['email'] == email

def test_invalid_load_user(user_class):
    assert user_class.load_user("invalid_value") == False

def test_invalid_and_continued_load_user(user_class):
    assert user_class.load_user(user_id="invalid_value") == False
    assert user_class.get_user() == False

def test_ambiguous_load(user_class):
    with pytest.raises(Exception):
        user_class.load_user(user_id="value", email="value")

@pytest.mark.dependency(depends=['test_ambiguous_load'])
def test_premature_load_user(user_class):
    assert user_class.get_user() == False
