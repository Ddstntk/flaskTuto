from flask import Flask
from config import Config
<<<<<<< HEAD

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
=======
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes
from app import models
>>>>>>> 6d89c72c3471fde89a361ec9709c478bc9e19a08
