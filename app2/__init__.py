from flask import Flask, render_template, redirect, url_for, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app2 import routes, models
db.create_all()
db.session.commit()
