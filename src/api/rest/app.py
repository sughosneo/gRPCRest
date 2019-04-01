'''
    This app.py script would act as the rest API server.
    It has been written based on falcon rest framework.

    - After fetching the params from the get request it actually makes a call to gRPC server to fetch the result.
'''

import grpc

import json
from wsgiref import simple_server
import falcon
import requests

# gRPC related class files which needs to be imported in both server and client side.
import CustomerInfoSvc_pb2 as CustomerInfoSvc_pb2
import CustomerInfoSvc_pb2_grpc as CustomerInfoSvc_pb2_grpc

# Library to format any protobuf to json or back to protobuf.
from google.protobuf import json_format

class CustomerManagerResource:

    '''
        only on_get() method has been implemented.
    '''
    def on_get(self, req, resp,customer_id):

        try:

            # This is the parameter which is going to get passed.
            customerId = customer_id
            customerPersonalInfo = self.__getCustomerPersonInfo(customerId)

            resp.status = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
            resp.body = json.dumps({"result":"success","details" : customerPersonalInfo})

        except Exception as error:

            print(error)
            resp.status = falcon.HTTP_500
            resp.body = json.dumps({"result" : "failed", "details" : falcon.HTTPInternalServerError("Unable to create task")})

    '''
        This method would actually talk to the gRPC server to fetch the customer details.        
    '''
    def __getCustomerPersonInfo(self,customerId):

        if customerId :

            channel = grpc.insecure_channel('0.0.0.0:50051')

            stub = CustomerInfoSvc_pb2_grpc.CustomerInfoSvcStub(channel)

            try:

                # As the gRPC is going to accept a int params. So typecasting it before sending the actual request.
                # If any other integer value been passed apart from 777 it would throw the error.
                response = stub.getCustomerInformation(CustomerInfoSvc_pb2.CustomerInfoSvcRequest(customerId=int(customerId)))
                print(response)
                print("Converting this response Customer obj to json !")
                return json_format.MessageToJson(response.customer)

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
        else:
            raise Exception(falcon.HTTPInvalidParam("customer_id params value is not correct !"))


appManager = falcon.API()
customerMgrResourceObj = CustomerManagerResource()
appManager.add_route("/manage/customer/{customer_id}/info",customerMgrResourceObj)


if __name__ == '__main__':
    httpd = simple_server.make_server('0.0.0.0', 8000, appManager)
    print("API has been started and listening on http://0.0.0.0:8000/manage/customer/{customer_id}/info")
    httpd.serve_forever()
