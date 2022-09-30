from decouple import config
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routs import routs


class ProductionConfig:
    FLASK_ENV = 'prod'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@localhost:{config("DB_PORT")}/{config("DB_NAME")}'
    )


class DevelopmentConfig:
    FLASK_ENV = 'prod'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@localhost:{config("DB_PORT")}/{config("DB_NAME")}'
    )


def create_app(conf='config.DevelopmentConfig'):
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(conf)
    migrate = Migrate(app, db)

    api = Api(app)
    [api.add_resource(*rout) for rout in routs]
    return app


