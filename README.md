# gRPCRest - (Still In Making)
Project to showcase example on gRPC and Rest endpoint


##### Writing Rest - JSON based API
    - Define app.py which would hold the server.
    - Define the request.
    
    
##### Defining CustomerInfoSvc gRPC Server & Test Client. Below are the steps :

    - Define a service in a .proto file.
    - Generate server and client code using the protocol buffer compiler.
    - Use the Python gRPC API to write a simple client and server for your service.
    
    $ pip install grpcio
    $ pip install grpcio-tools
    
    $ cd /projects/gRPCRest/src/api/gRPC/protos/
    $ python -m grpc_tools.protoc  -I.  --python_out=. --grpc_python_out=. CustomerInfoSvc.proto
    