# Use the official Python slim image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file from the root folder
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# DO NOT hardcode ENV PORT. Cloud Run will inject this automatically.
EXPOSE 8080

# Use a shell execution command to dynamically read the Cloud Run $PORT variable
CMD ["sh", "-c", "streamlit run app.py --server.port=${PORT:-8080} --server.address=0.0.0.0"]