import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    LANGUAGES = ['en', 'ru', 'uk']
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

    GOOGLE_MAPS_API_KEY = 'AIzaSyDMjp6-KGpAQNdipQEcSEbBPo2DCeey2rc'

    ACCUWEATHER_API_KEY = 'Ywafhzvrhr3p4k8gNqFt4wOZk5lD2Ani'
    ACCUWEATHER_LANGUAGE = 'en-us'
    ACCUWEATHER_BASIC_URL = 'https://dataservice.accuweather.com/'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'besmertn@gmail.com'
    MAIL_PASSWORD = 'z9hn4goqb'
    ADMINS = 'besmertn@gmail.com'
