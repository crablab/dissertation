import datetime
from .. import db, flask_bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

__all__ = ['user']

class user(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text(), nullable=False)
    username = db.Column(db.Text(), nullable=False)
    _password = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text(), nullable=False)
    enabled = db.Column(db.Integer())
    created = db.Column(db.DateTime,
            default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime,
        default=datetime.datetime.utcnow)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = flask_bcrypt.generate_password_hash(
            password)

    def get_id(self):
        return self.id
