from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aabcbb8bf275c9d1a503d6ab3793590d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # /// is relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #turning off the warning, we're just using for practice.

db = SQLAlchemy(app)

from flaskblog import routes