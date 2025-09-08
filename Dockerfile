FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY models/ ./models/

EXPOSE 5672

CMD ["fastapi", "run", "src/web_server.py"]