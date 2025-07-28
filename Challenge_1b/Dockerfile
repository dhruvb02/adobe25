# Use the official Python 3.13 slim image as a base
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's layer caching
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files into the container
COPY process.py .
COPY persona.json .
COPY input/ ./input/

# Create the output directory where results will be stored
RUN mkdir -p /app/output

# Set the command to run your script when the container starts
CMD ["python", "process.py"]