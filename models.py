# Description: This file contains the database models for the application.


# Importing the necessary libraries
from flask_sqlalchemy import SQLAlchemy


# Creating the database object
db = SQLAlchemy()


class User(db.Model):
    """
    Creating the User model
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    high_score = db.Column(db.Integer, default=0)


class Question(db.Model):
    """
    Creating the Question model
    """
    
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    answer_a = db.Column(db.String(100), nullable=False)
    answer_b = db.Column(db.String(100), nullable=False)
    answer_c = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)