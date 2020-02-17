import pytest, cuid

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

    assert user_class.create_user(name, email, password, type) != False

def test_login_student_user(user_class, email):
    password = "test"

    assert user_class.check_login(email, password) == True


