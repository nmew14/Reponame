# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables for security
ENV BOT_TOKEN=""
ENV API_ID=""
ENV API_HASH=""
ENV USER_ID=""

# Run bot
CMD ["python", "bot.py"]
