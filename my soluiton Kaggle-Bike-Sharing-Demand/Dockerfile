FROM python:3.9-slim-buster

# Make a Dir for our application
WORKDIR /flask app

# Install requirments
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy our source code
COPY app/ .

# Run the application
CMD ["python", "main.py"]