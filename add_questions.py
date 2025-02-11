# Description: This script adds AI-related questions to the database.


# Importing the necessary libraries
from models import db, Question
from app import app


# AI-related questions
questions = [
    Question(
        question_text="Which Python library is commonly used for deep learning?",
        answer_a="TensorFlow",
        answer_b="Flask",
        answer_c="Pandas",
        correct_answer="A"
    ),
    Question(
        question_text="What does NLP stand for in AI?",
        answer_a="Neural Learning Processing",
        answer_b="Natural Language Processing",
        answer_c="Network Layer Protocol",
        correct_answer="B"
    ),
    Question(
        question_text="Which Python library is best suited for computer vision tasks?",
        answer_a="OpenCV",
        answer_b="Scikit-learn",
        answer_c="BeautifulSoup",
        correct_answer="A"
    ),
    Question(
        question_text="Which algorithm is commonly used for text classification?",
        answer_a="K-Means",
        answer_b="Naive Bayes",
        answer_c="Dijkstra's Algorithm",
        correct_answer="B"
    ),
    Question(
        question_text="Which Python library provides pre-trained AI models like GPT-3?",
        answer_a="Hugging Face Transformers",
        answer_b="Matplotlib",
        answer_c="PyTorch",
        correct_answer="A"
    )
]


# Insert AI-related questions into the database
with app.app_context():
    db.session.add_all(questions)
    db.session.commit()
    print("AI-related quiz questions added successfully!")
