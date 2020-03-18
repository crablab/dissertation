import pytest, cuid

@pytest.fixture(scope='session')
def upcoming_lectures():
    from ..libraries import upcoming_lectures
    return upcoming_lectures.upcoming_lectures()