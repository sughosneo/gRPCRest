import grpc
from concurrent import futures
import time

# Importing compiled protobuf related files.
import gRPCRest.src.api.gRPC.protos.CustomerInfoSvc_pb2 as CustomerInfoSvc_pb2
import gRPCRest.src.api.gRPC.protos.CustomerInfoSvc_pb2_grpc as CustomerInfoSvc_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# Class contains the server functions, derived from CustomerInfoSvc_pb2_grpc.CustomerInfoSvcServicer
class CustomerInformation(CustomerInfoSvc_pb2_grpc.CustomerInfoSvcServicer):

    def getCustomerInformation(self, request, context):

        customerId = request.customerId

        # If customer id value is 777 valid
        if customerId == 777:

            context.set_details("Customer information found !")
            context.set_code(grpc.StatusCode.OK)
            return CustomerInfoSvc_pb2.CustomerInfoSvcResponse.Customer

        else:

            context.set_details("Customer Id is not valid !")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)

            return CustomerInfoSvc_pb2.CustomerInfoSvcResponse()

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    CustomerInfoSvc_pb2_grpc.add_CustomerInfoSvcServicer_to_server(CustomerInformation(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
