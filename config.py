import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Best Practice of how to lauch configuration for your Flask App, check Flask documentation

    Here you set all your flask configuration environment that is common to Development, Testing and Production
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    Inherits from class config to take its variables and also add some of its own specific configuration
    like the database configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(str(basedir), \
                                                                                                'data-dev.sqlite')


class TestingConfig(Config):
    """
    This is the testing configuration
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(str(basedir), \
                                                                                                'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL') or 'sqlite:///' + os.path.join(str(basedir), \
                                                                                                'data-prod.sqlite')


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,

    "default": DevelopmentConfig
}
