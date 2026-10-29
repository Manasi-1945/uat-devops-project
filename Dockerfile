FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir --timeout=120 --retries=5 pytest

COPY hello.py .
COPY test_hello.py .

CMD ["python", "hello.py"]