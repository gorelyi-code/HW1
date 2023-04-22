FROM ubuntu:latest

WORKDIR protobuf

ADD lib lib
COPY scripts/protobuf/main.py .
COPY scripts/protobuf/structure.proto .
COPY scripts/protobuf/requirements.txt .

RUN apt-get -y update && apt-get -y install python3 python3-pip curl unzip

RUN curl -Lo protoc.zip https://github.com/protocolbuffers/protobuf/releases/download/v22.3/protoc-22.3-linux-x86_64.zip

RUN unzip -o protoc.zip -d /usr/local bin/protoc

RUN protoc --python_out=. structure.proto

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]