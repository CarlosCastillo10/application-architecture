from decouple import config


class Config(object):
    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # Set up the SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='s3gund0p@rcial_002')

    # Mysql database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='mysql+pymysql'),
        config('DB_USERNAME', default='parcialb1_admin'),
        config('DB_PASS', default='parcial02b1'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=3307),
        config('DB_NAME', default='parcial_b1')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False


config_dict = {'config': Config}
