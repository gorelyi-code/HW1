FROM python:latest

WORKDIR yaml

ADD lib lib
COPY scripts/yaml/requirements.txt .
COPY scripts/yaml/main.py .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]