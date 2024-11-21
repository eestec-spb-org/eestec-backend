FROM python:3.11-slim

COPY . .

RUN pip install -r requirements.txt
RUN pip install passlib asyncpg python-multipart

EXPOSE 5049
CMD uvicorn app.main:app --host 0.0.0.0 --port 5049