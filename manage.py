from flask import Flask
from flask_migrate import Migrate

from app.main.controller.app_controller import controller_blueprint
from app.main.model.models import db

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:postgres@flask_postgres_db:5432/postgres',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(controller_blueprint)

if __name__ == '__main__':
    app.run(debug=True)