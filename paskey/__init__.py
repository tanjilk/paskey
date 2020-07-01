from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '77b4411ad78eec3ed211df19637a2d9a'
app.config['SQLALCHEMY_DATABASE_URI'] = '	postgres://fsaoycxj:LNub2YkW9FJMrH2EqiSHs3ukGgfSCoax@ruby.db.elephantsql.com:5432/fsaoycxj'
db = SQLAlchemy(app)

from paskey import routes
