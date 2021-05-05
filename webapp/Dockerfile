FROM python:3.9

# Make directory for application
RUN mkdir /app

# Copy application files to /app
COPY requirements.txt /app
COPY server.py /app
COPY index.html /app

# Install dependencies using pip
RUN pip install -r /app/requirements.txt

# Expose ports
EXPOSE 80

# Set the working directory of the container to /app
WORKDIR /app

# Run the server
ENTRYPOINT ["python", "/app/server.py"]
