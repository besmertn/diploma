import enum
from time import time

import jwt
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from diploma import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_id(self):
        return self.id

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        if not self.password_hash:
            return None
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            _id = jwt.decode(token, current_app.config['SECRET_KEY'],
                             algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(_id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class SensorStatus(int, enum.Enum):
    NOT_RESPONDING = 0
    ACTIVE = 1
    NOT_ACTIVE = 2

    @staticmethod
    def as_dict():
        return {0: 'Not Responding', 1: 'Active', 2: 'Not Active'}


class SyncType(int, enum.Enum):
    EACH_DAY = 0
    EACH_12_HOURS = 1
    EACH_6_HOURS = 2
    EACH_3_HOURS = 3
    HOURLY = 4

    @staticmethod
    def as_dict():
        return {0: 'Each day', 1: 'Each 12 Hours', 2: 'Each 6 Hours', 3: 'Each 3 Hours', 4: 'Hourly'}


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True)
    region_key = db.Column(db.Integer, index=True)
    region_name = db.Column(db.String(128))
    coordinates = db.Column(db.String(128))
    status = db.Column(db.Enum(SensorStatus), index=True, )
    sync_type = db.Column(db.Enum(SyncType))
    is_shared = db.Column(db.Boolean, index=True, default=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in Sensor.__table__.columns}
