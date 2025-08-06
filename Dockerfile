# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install required system packages
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Set environment variables (optional)
# ENV HF_TOKEN=your_token_here

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
