# py_feedparser_grpc
Feed Parsing gRPC API written in python

#### Run server
`PORT=50051 python feedster_server.py`

#### Run sample client
`python feedster_client.py`


#### Compile ProtoBuf
`$ python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/feedster.proto`

### Build

    export GCP_PROJECT=markeev-pro
    docker build -t gcr.io/$GCP_PROJECT/grpc-feedster:latest .

    gcloud builds submit --tag gcr.io/$GCP_PROJECT/grpc-feedster
