# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
#RUN apt-get install python3-django
# Copy the rest of the application code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Set the default command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

