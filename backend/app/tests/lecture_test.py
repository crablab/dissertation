import pytest
from datetime import datetime

@pytest.fixture(scope='session')
def lecture_class():
    from ..libraries import lecture
    return lecture.lecture()

@pytest.fixture(scope='session')
def valid_datetime():
    return datetime.strptime("Jun 1 2020  2:15PM", "%b %d %Y %I:%M%p")

@pytest.fixture(scope='session')
def invalid_datetime():
    return datetime.strptime("Jun 1 2019  2:15PM", "%b %d %Y %I:%M%p")

@pytest.fixture(scope='session')
def string_datetime():
    return "Jun 1 2020  2:15PM"

@pytest.fixture(scope='session')
def now_datetime():
    return datetime.now()

@pytest.fixture(scope='session')
def course():
    return "CS1890"

def test_create_lecture(lecture_class, course, valid_datetime):
    id = lecture_class.create_lecture(course, valid_datetime)
    assert id != None
    assert lecture_class.course == course
    assert lecture_class.time == valid_datetime

def test_create_invalid_datetime_lecture(lecture_class, course, invalid_datetime):
    with pytest.raises(ValueError, match="Lecture cannot be in the past"):
        lecture_class.create_lecture(course, invalid_datetime)

def test_create_now_datetime_lecture(lecture_class, course, now_datetime):
    with pytest.raises(ValueError, match="Lecture cannot be in the past"):
        lecture_class.create_lecture(course, now_datetime)

def test_create_string_datetime(lecture_class, course, string_datetime):
    with pytest.raises(ValueError, match="Lecture datetime not a valid Datetime object"):
        lecture_class.create_lecture(course, string_datetime)

def test_manual_load_lecture(lecture_class, course, valid_datetime):
    id = lecture_class.create_lecture(course, valid_datetime)
    assert id != None
    assert lecture_class.load_lecture(id)
    assert lecture_class.course == course
    assert lecture_class.time == valid_datetime

def test_delete_lecture(lecture_class, course, valid_datetime):
    id = lecture_class.create_lecture(course, valid_datetime)
    assert id != None
    assert lecture_class.delete_lecture()