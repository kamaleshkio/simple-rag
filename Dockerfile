# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables to avoid permission issues
ENV HOME=/app
ENV HF_HOME=/app/hf_cache
ENV TRANSFORMERS_CACHE=/app/hf_cache/transformers
ENV STREAMLIT_CONFIG_DIR=/app/.streamlit

# Create necessary directories
RUN mkdir -p /app/.streamlit /app/hf_cache/transformers

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code into the container
COPY . .

# Expose Streamlit port
EXPOSE 7860

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.enableCORS=false"]
