import pytest, cuid
from datetime import datetime
from ..libraries import lectures
from ..libraries import lecture

@pytest.fixture(scope='session')
def lectures_class():
    return lectures.lectures()

@pytest.fixture(scope='session')
def lecture_class():
    return lecture.lecture()

@pytest.fixture(scope='session')
def course():
    idgen = cuid.CuidGenerator()
    return idgen.cuid()

@pytest.fixture(scope='session')
def valid_datetime():
    return datetime.strptime("Jun 1 2020  2:15PM", "%b %d %Y %I:%M%p")

@pytest.fixture(scope='session')
def lower_valid_datetime():
    return datetime.strptime("Jun 1 2020  1:15PM", "%b %d %Y %I:%M%p")

### TESTS ### 

def test_load_all_lectures(lectures_class):
    assert lectures_class.load_lectures() == True
    assert len(lectures_class.lectures) > 0

def test_load_course_lectures(lectures_class, lecture_class, course, valid_datetime):
    id1 = lecture_class.create_lecture(course, valid_datetime)
    id2 = lecture_class.create_lecture(course, valid_datetime)

    assert lectures_class.load_lectures(course) == True
    assert len(lectures_class.lectures) == 2
    assert lectures_class.lectures[id1].id == id1
    assert lectures_class.lectures[id2].id == id2

    lecture_class.load_lecture(id1)
    lecture_class.delete_lecture()
    lecture_class.load_lecture(id2)
    lecture_class.delete_lecture()

def test_load_datetime_lectures(lectures_class, lecture_class, course, valid_datetime, lower_valid_datetime):
    id1 = lecture_class.create_lecture(course, valid_datetime)
    id2 = lecture_class.create_lecture(course, lower_valid_datetime)

    assert lectures_class.load_lectures(course=course, time=valid_datetime) == True
    assert len(lectures_class.lectures) == 1
    assert lectures_class.lectures[id1].id == id1

    lecture_class.load_lecture(id1)
    lecture_class.delete_lecture()
    lecture_class.load_lecture(id2)
    lecture_class.delete_lecture()