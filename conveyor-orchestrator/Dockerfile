# Use an official Python 3.12 slim runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

# Set the working directory
WORKDIR /workspace

# Copy dependencies list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the default Cloud Run port
EXPOSE 8080

# Start the uvicorn server pointing to our FastAPI app
CMD ["sh", "-c", "uvicorn app.fast_api_app:app --host 0.0.0.0 --port ${PORT}"]
