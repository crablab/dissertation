from ..libraries import user 
from sqlalchemy.orm import sessionmaker

def test_create_user(session):
    """Creates a new user"""

    email = 'test@example.com'
    username = 'test_user'
    password = 'foobarbaz'

    new_user = user(email, username, password)
    session.add(user)
    session.commit()

    assert new_user.id is not None