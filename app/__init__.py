# app/__init__.py

import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/health_app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key'

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import main
    from app.api import api

    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    return app
