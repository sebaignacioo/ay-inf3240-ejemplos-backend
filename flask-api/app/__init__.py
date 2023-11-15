from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import DeclarativeBase

from config import SQLAlchemyConfig

app = Flask(__name__)
app.config.from_object(SQLAlchemyConfig)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app, model_class=Base)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

from app.routes import auth as auth_routes
from app.routes import documento as documento_routes

app.register_blueprint(auth_routes.auth_bp)
app.register_blueprint(documento_routes.doc_bp)

with app.app_context():
    db.create_all()