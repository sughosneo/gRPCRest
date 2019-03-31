'''
    This is the gRPC CustomerInfoSvc server file which holds the implementation of
    getCustomerInformation() method.
'''
import grpc
from concurrent import futures
import time

# Importing compiled protobuf related files.
import CustomerInfoSvc_pb2
import CustomerInfoSvc_pb2_grpc
import Customer_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# Class contains the server functions, derived from CustomerInfoSvc_pb2_grpc.CustomerInfoSvcServicer
class CustomerInformation(CustomerInfoSvc_pb2_grpc.CustomerInfoSvcServicer):

    def getCustomerInformation(self, request, context):

        customerId = request.customerId

        # If customer id value is 777 valid
        if customerId == 777:

            context.set_details("Customer information found !")
            context.set_code(grpc.StatusCode.OK)

            customerDetails = Customer_pb2.Customer()
            customerDetails.firstName = "Sumit"
            customerDetails.lastName = "Ghosh"
            customerDetails.emailId = "abc@foo.com"

            return CustomerInfoSvc_pb2.CustomerInfoSvcResponse(customer=customerDetails)

        else:

            context.set_details("Customer Id is not valid !")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)

            return CustomerInfoSvc_pb2.CustomerInfoSvcResponse()

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    CustomerInfoSvc_pb2_grpc.add_CustomerInfoSvcServicer_to_server(CustomerInformation(), server)
    print("gRPC server is starting...")
    print("Listening on - rpc://0.0.0.0:50051",)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
