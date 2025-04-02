FROM python:3.8-slim

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy test files
COPY . /tests
WORKDIR /tests
# Command to run tests
CMD ["pytest", "-v"]
