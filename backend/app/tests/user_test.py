import pytest

@pytest.fixture
def user_class():
    from ..libraries import user
    return user.user()

def test_create_student_user(user_class):
    name = "Joe Bloggs"
    email = "joe@live.rhul.ac.uk"
    password = "test"
    type = "student"

    user_class.create_user(name, email, password, type)