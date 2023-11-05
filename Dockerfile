# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE myproject.settings

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Install project dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Expose the port your Django app will run on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
