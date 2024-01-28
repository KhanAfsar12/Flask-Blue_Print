from flask import Flask
from .database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/account'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)

from app import routes