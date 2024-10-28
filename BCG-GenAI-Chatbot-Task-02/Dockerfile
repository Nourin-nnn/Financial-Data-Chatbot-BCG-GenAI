# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000


# Define the command to run the app
CMD ["python", "chatbot_flask.py"]
