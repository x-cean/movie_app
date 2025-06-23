from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from datamanager.sqlite_data_manager import SQLiteDataManager
from datamanager.sql_data_models import db, User, Movie


DATABASE_URL = "sqlite:///data/data.sqlite"


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db.init_app(app)
