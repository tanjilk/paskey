from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '77b4411ad78eec3ed211df19637a2d9a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://paskey:password@db4free.net:3306/paskey'
db = SQLAlchemy(app)

from paskey import routes
