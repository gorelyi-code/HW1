FROM python:latest

WORKDIR avro

ADD lib lib
COPY scripts/avro/requirements.txt .
COPY scripts/avro/main.py .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]