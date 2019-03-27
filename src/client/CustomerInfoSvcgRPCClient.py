import grpc

# Importing compiled protobuf related files.
import gRPCRest.src.api.gRPC.protos.CustomerInfoSvc_pb2 as CustomerInfoSvc_pb2
import gRPCRest.src.api.gRPC.protos.CustomerInfoSvc_pb2_grpc as CustomerInfoSvc_pb2_grpc

def run():

    channel = grpc.insecure_channel('localhost:50051')
    stub = CustomerInfoSvc_pb2_grpc.CustomerInfoSvc_pb2_grpc(channel)

    try:

        # If any other integer value been passed apart from 777 it would throw the error.
        response = stub.SayHelloStrict(CustomerInfoSvc_pb2.CustomerInfoSvcRequest(customerId=777))
        print(response.Result)

    except grpc.RpcError as e:

        print(e.details())
        # Let's access the error code, which is `INVALID_ARGUMENT`
        # `type` of `status_code` is `grpc.StatusCode`
        status_code = e.code()
        # should print `INVALID_ARGUMENT`
        print(status_code.name)
        print(status_code.value)

        # If you want to perform any specific action.
        if grpc.StatusCode.INVALID_ARGUMENT == status_code:
            # You can incorporate your customer module in here.
            pass

if __name__ == '__main__':
    run()