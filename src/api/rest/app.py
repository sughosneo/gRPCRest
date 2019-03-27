import json
from wsgiref import simple_server
import falcon
import requests

from TaskRequestMgrObjModel import *
from UtilityHelper import *

class CustomerManagerResource:

    def on_get(self, req, resp):

        try:

            resp.status = falcon.HTTP_200
            customerPersonalInfo = self.__getCustomerPersonInfo()
            resp.body = json.dumps({"result":"success","description" : "Task has been created successfully !"})

        except Exception as error:

            print(error)
            resp.status = falcon.HTTP_500
            resp.body = json.dumps({"result" : "failed", "description" : falcon.HTTPInternalServerError("Unable to create task")})

    def __getCustomerPersonInfo(self):

        try:
            pass
        except Exception as error:
            print(error)


appManager = falcon.API()
customerMgrResourceObj = CustomerManagerResource()
appManager.add_route("/manage/customer/info",customerMgrResourceObj)


if __name__ == '__main__':
    httpd = simple_server.make_server('localhost', 8000, appManager)
    print("API has been started and listening on http://0.0.0.0:8000/manage/customer/info")
    httpd.serve_forever()
