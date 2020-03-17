import pytest, cuid
from datetime import datetime
from ..libraries import allocation
from ..libraries import lecture
from ..libraries import user

@pytest.fixture()
def allocation_class():
    return allocation.allocation()

@pytest.fixture()
def lecture_class():
    return lecture.lecture()

@pytest.fixture(scope='session')
def user_class():
    return user.user()

@pytest.fixture()
def course():
    idgen = cuid.CuidGenerator()
    return idgen.cuid()

@pytest.fixture()
def random_value():
    idgen = cuid.CuidGenerator()
    return idgen.cuid()

@pytest.fixture(scope='session')
def valid_datetime():
    return datetime.strptime("Jun 1 2020  2:15PM", "%b %d %Y %I:%M%p")

@pytest.fixture()
def created_user(user_class, random_value):
    return user_class.create_user("Test " + random_value, random_value + ".test@live.rhul.ac.uk", random_value, "student")

### TESTS ### 

def test_allocate_student_course(allocation_class, lecture_class, course, valid_datetime, created_user):
    lecture_class.create_lecture(course, valid_datetime)
    assert allocation_class.allocate(created_user, course) != False

def test_allocate_student_course_multiple(allocation_class, lecture_class, course, valid_datetime, created_user):
    lecture_class.create_lecture(course, valid_datetime)
    assert allocation_class.allocate(created_user, course) != False
    assert allocation_class.allocate(created_user, course) == False

def test_allocate_student_missing_course(allocation_class, created_user, random_value):
    assert allocation_class.allocate(created_user, random_value) == False

def test_allocate_student_missing_user(allocation_class, random_value, course):
    assert allocation_class.allocate(random_value, course) == False

def test_load_allocation_manual_load(allocation_class, lecture_class, course, valid_datetime, created_user):
    lecture = lecture_class.create_lecture(course, valid_datetime)
    id = allocation_class.allocate(created_user, course)
    allocation_class.load_allocation(id)
    assert allocation_class.id == id
    assert allocation_class.course == course
    assert allocation_class.user == created_user

def test_load_allocation_autoload(allocation_class, lecture_class, course, valid_datetime, created_user):
    lecture = lecture_class.create_lecture(course, valid_datetime)
    id = allocation_class.allocate(created_user, course)
    assert allocation_class.id == id
    assert allocation_class.course == course
    assert allocation_class.user == created_user

def test_check_allocation(allocation_class, lecture_class, course, valid_datetime, created_user):
    lecture = lecture_class.create_lecture(course, valid_datetime)
    id = allocation_class.allocate(created_user, course)
    assert allocation_class.check_allocation(created_user, course) == True

def test_check_allocation_false(allocation_class, lecture_class, course, valid_datetime, created_user, random_value):
    lecture = lecture_class.create_lecture(course, valid_datetime)
    id = allocation_class.allocate(created_user, course)
    assert allocation_class.check_allocation(random_value, course) == False