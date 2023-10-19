from app.main.model.models import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.main.controller.app_controller import controller_blueprint
import os

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:postgres@localhost:5433/postgres',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
migrate = Migrate(app, db)
db.init_app(app)
app.register_blueprint(controller_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
