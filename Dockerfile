# Use the official Python image as the base image
FROM python:3.11

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE 0

# Install Poetry
RUN pip install poetry==1.2.2

# Set the working directory in the container
WORKDIR /app

# Copy your Django project files into the container
COPY . /app/

# Install Python dependencies with Poetry
RUN poetry install --without dev,scripts

# Collect static files 
RUN python manage.py collectstatic --noinput

# Expose the port on which Django will run (if using the development server)
EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "tamedrift.wsgi"]