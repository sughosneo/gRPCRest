'''

    This is the sample client script which would talk to the gRPC server directly
        and get the response back based on the request params.

'''
import grpc

# Importing compiled protobuf related files.
# This files are required in both client and server side.
import CustomerInfoSvc_pb2 as CustomerInfoSvc_pb2
import CustomerInfoSvc_pb2_grpc as CustomerInfoSvc_pb2_grpc

from google.protobuf import json_format

def run():

    channel = grpc.insecure_channel('localhost:50051')
    stub = CustomerInfoSvc_pb2_grpc.CustomerInfoSvcStub(channel)

    try:

        # If any other integer value been passed apart from 777 it would throw the error.
        response = stub.getCustomerInformation(CustomerInfoSvc_pb2.CustomerInfoSvcRequest(customerId=777))
        print(response)
        print("Converting this response Customer obj to json !")
        print(json_format.MessageToJson(response.customer))

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
            print("INVALID_ARGUMENT - error has come up !")

if __name__ == '__main__':
    run()