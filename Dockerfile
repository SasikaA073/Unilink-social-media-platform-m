# UniLink Project

# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file separately to leverage Docker cache
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

# Install dependencies
RUN pip install pipenv
RUN pipenv install --deploy --system

# Copy the entire project directory to the working directory in the container
COPY . /code/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]