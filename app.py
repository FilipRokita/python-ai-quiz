# Description: This file is the main file that runs the Flask application. It contains the routes for the application.


# Importing the necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, Question
import os


# Creating the Flask application
app = Flask(__name__)

# Reloading the templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure the database
db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


