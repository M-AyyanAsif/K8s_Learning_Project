# Use the slim python image to keep size minimum (~120MB)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies (no-cache-dir keeps the image size down)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the requested port
EXPOSE 5800

# Run Streamlit on port 5800
CMD ["streamlit", "run", "app.py", "--server.port=5800", "--server.address=0.0.0.0"]