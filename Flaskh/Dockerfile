# Use the official Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . .

# Expose the desired port
EXPOSE 5000

# Set the command to run the Flask application
CMD ["flask", "run", "--host", "0.0.0.0"]
