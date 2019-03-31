# gRPCRest - (Still In Making)
This sample project is basically to showcase proper examples on gRPC , Rest endpoint and communication between them.
Ideally in production scenario you may not see communication a rest on top of gRPC server. That's the reason in this project, there is a separate client to 
test out the gRPC server implementation. But intend here to demo multiple possibilities and it's possible implementation.


## How to set up this project ?

    #### Using in your windows/mac/ubuntu env :
   
    - git clone <repo_git_url>
    - cd /gRPCRest/src/
    - Go to the specific folder
    - python3 <gRPC_server_script_name> / It would run on 50051 port
    - python3 <rest_server_script_name> / It would run on 50051 port
    
    
   #### Using docker env :
   
    - git clone <repo_git_url>
    - cd /dsalgo/
    - docker build -t sughosneo/dsalgo .
    - docker run -it sughosneo/dsalgo /bin/bash


## Details about repo / code base :
<!-------------------------------------------------->

##### Writing Rest - JSON based API :
    - Define app.py which would hold the server.
    - Define the request.
    
    
##### Defining CustomerInfoSvc gRPC Server. Below are the steps :

    - Define a service in a .proto file.
    - Generate server and client code using the protocol buffer compiler.
    - Use the Python gRPC API to write a simple client and server for your service.
    
    - Below steps to help to generate required python class files from proto data structures.
    
    $ pip install grpcio
    $ pip install grpcio-tools
    
    $ cd /projects/gRPCRest/src/api/gRPC/protos/
    $ python -m grpc_tools.protoc  -I.  --python_out=.. --grpc_python_out=. CustomerInfoSvc.proto
    $ python -m grpc_tools.protoc  -I.  --python_out=.. --grpc_python_out=. Customer.proto
    
    - After running the above commands it would create respective python packages under gRPC folder.
    - These generated python class files would be required to reference in gRPC communication between client and server.
    
##### Test Client(s) :

    - For the rest API this project has a separate client - "CustomerInfoSvcRestClient" 
    - And for the gRPC server there is a separate "CustomerInfoSvcgRPCClient"
    

 
