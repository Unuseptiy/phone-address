FROM python:3.11-alpine
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN mkdir app
COPY . /app
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000
