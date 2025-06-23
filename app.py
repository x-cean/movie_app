import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

from datamanager.sqlite_data_manager import SQLiteDataManager
from datamanager.sql_data_models import db, User, Movie


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data', 'data.sqlite')


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app) # links the instance of SQLAlchemy to the Flask application instance app

# create tables if they do not exist
with app.app_context():
    inspector = inspect(db.engine)
    if not inspector.get_table_names():
        db.create_all()

data_manager = SQLiteDataManager(db)

with app.app_context():
    users = data_manager.get_all_users()
    print(users)