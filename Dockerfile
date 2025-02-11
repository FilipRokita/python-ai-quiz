# Use Python 3.12-slim as the base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8082

# Use an entrypoint script to initialize the app
ENTRYPOINT ["bash", "./entrypoint.sh"]

# Command to run the application
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8082", "app:app"]