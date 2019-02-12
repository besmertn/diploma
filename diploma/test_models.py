import pytest

from diploma import app, db
from diploma.models import User


@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.create_all()
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

    db.session.remove()
    db.drop_all()


def test_password_hashing():
    u = User(username='susan')
    u.set_password('cat')
    assert not u.check_password('dog')
    assert u.check_password('cat')
