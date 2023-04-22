FROM python:latest

WORKDIR xml

ADD lib lib
COPY scripts/xml/requirements.txt .
COPY scripts/xml/main.py .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]