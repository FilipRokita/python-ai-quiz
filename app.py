# Description: This file is the main file that runs the Flask application. It contains the routes for the application.


# Importing the necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from models import db, User, Question
import os
from datetime import datetime


# Creating the Flask application
app = Flask(__name__)

# Reloading the templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Index route, main route of the application.
    """

    # (WHEN METHOD = POST) Check if the form was submitted
    if request.method == "POST":
        # Get the username from the form (if it exists)
        username = request.form.get("username")
        if not username:
            return "Error: Please enter your name!", 400
        
        # Save the username in the session
        session["username"] = username
        
        # Get questions from the database
        questions = Question.query.all()  # Get all the questions
        score = 0
        total_questions = len(questions)

        # Loop through the questions
        for question in questions:
            user_answer = request.form.get(f"question_{question.id}")  # Get the user's answer
            # Check if the user's answer is correct
            if user_answer and user_answer == question.correct_answer:
                score += 1

        # Compute the percentage score
        final_score = int((score / total_questions) * 100)

        # Get/add the user from/to the database
        user = User.query.filter_by(username=username).first()  # Get the user from the database
        # If the user does not exist, create a new user
        if not user:
            user = User(username=username)
            db.session.add(user)
        # If the user exists, update the their high score (if it's higher)
        elif final_score > user.high_score:
                user.high_score = final_score
        # Commit the changes to the database
        db.session.commit()

        # Return the results
        return render_template("results.html", username=username, score=final_score, high_score=user.high_score)

    # WHEN METHOD = GET
    # Get questions from the database
    questions = Question.query.all()

    # Get the user's high score from the database
    username = session.get("username")
    best_score = 0
    if username:
         user = User.query.filter_by(username=username).first()
         best_score = user.high_score if user else 0

    return render_template("index.html", best_score=best_score, questions=questions)


# Run the application
if __name__ == "__main__":
    app.run(debug=True)