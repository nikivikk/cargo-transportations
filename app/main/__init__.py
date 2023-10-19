# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# from flask.app import Flask
#
# db = SQLAlchemy()
#
#
# def create_app() -> Flask:
#     app = Flask(__name__)
#
#     app.config.update(
#         SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:postgres@localhost:5433/postgres',
#         # SQLALCHEMY_TRACK_MODIFICATIONS=False,
#         DEBUG=True
#     )
#     db.init_app(app)
#
#     return app
