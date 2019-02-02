import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_LOGIN_CLIENT_ID = "294712924433-gta750bbu0te47h0p8s268bnu2m9dr9g.apps.googleusercontent.com"
    GOOGLE_LOGIN_CLIENT_SECRET = "xrM_06uRI28tsTQl-kDAx7no"

    OAUTH_CREDENTIALS = {
        'google': {
            'id': GOOGLE_LOGIN_CLIENT_ID,
            'secret': GOOGLE_LOGIN_CLIENT_SECRET
        }
    }
