from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Setup Temp Db for Sql Inj

db = SQLAlchemy()


def setup_app():
    # Setup App
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

