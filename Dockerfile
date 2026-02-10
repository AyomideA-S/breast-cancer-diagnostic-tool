# Use the slim version of Python 3.12 as the base image
FROM python:3.12.12-slim

# Set the working directory
WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Run Streamlit pointing to the src folder
# Note: Streamlit uses --server.port and --server.address flags
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]