FROM python:3-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
# Copy application code
COPY . /app
WORKDIR /app

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# Expose the application port
EXPOSE 8000

# Start the Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]