# Description: This file is used to initialize the database and the app.


# Importing the necessary libraries
from models import db
from app import app


# Creating the database
with app.app_context():
    db.create_all()
    print("Database initialized successfully.")