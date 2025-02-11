# Description: This file is used to initialize the database and the app.


# Importing the necessary libraries
from models import db
from app import app
import os


# Database path
db_path = os.path.join("instance", "quiz.db")

# Removing the database file if it exists
if os.path.exists(db_path):
    os.remove(db_path)
    print("Database file removed successfully.")

# Creating the database
with app.app_context():
    db.create_all()
    print("Database initialized successfully.")