# Based on textbook examples: https://learning.oreilly.com/library/view/flask-blueprints/9781784394783/ch04s05.html

import pytest
from . import create_app, db as database

@pytest.fixture
def app():
    app = create_app(config='test_settings')
    return app

@pytest.fixture(scope='session')
def db(app, request):

    database.app = app
    database.create_all()

    def teardown():
        database.drop_all()
        os.unlink(DB_LOCATION)
    request.addfinalizer(teardown)
    return database


@pytest.fixture(scope='function')
def session(db, request):

    session = db.create_scoped_session()
    db.session = session

    def teardown():
        session.remove()

    request.addfinalizer(teardown)
    return session