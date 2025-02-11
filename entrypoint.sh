#!/bin/bash

# Check if the database file exists
if [ ! -f "./instance/quiz.db" ]; then
  echo "Database does not exist. Starting setup..."
  # Run the database initialization script and add questions
  python init_db.py
  python add_questions.py
  echo "Database setup complete."
else
  echo "Database already exists. Skipping setup..."
fi

# Execute the command passed as arguments (CMD from Dockerfile)
exec "$@"