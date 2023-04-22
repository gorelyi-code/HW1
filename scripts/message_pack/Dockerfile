FROM python:latest

WORKDIR message_pack

ADD lib lib
COPY scripts/message_pack/requirements.txt .
COPY scripts/message_pack/main.py .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]