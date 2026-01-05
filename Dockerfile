# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependencies file first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose Flask port
EXPOSE 5001

# Run the Flask app
CMD ["python", "app.py"]
