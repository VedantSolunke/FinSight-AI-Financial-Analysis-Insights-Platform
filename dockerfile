# Use a lightweight Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

RUN pip install uv

COPY requirements.txt ./

# Install the required Python packages
RUN uv pip install --system -r requirements.txt

# Copy the application code into the container
COPY . /app

# Expose the port that the application will run on
EXPOSE 8000

#USE uvicorn to run the FastAPI application defined in app.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


