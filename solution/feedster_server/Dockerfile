FROM python:3.8

WORKDIR /srv/grpc

COPY feedster_server.py protos/*.proto requirements.txt ./

RUN pip install -r requirements.txt && \
    python -m grpc_tools.protoc \
        -I. \
        --python_out=. \
        --grpc_python_out=. \
        feedster.proto

EXPOSE 50051

CMD ["python", "feedster_server.py"]