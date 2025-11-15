# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the port the app runs on
EXPOSE 5000

# Run the application using gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
