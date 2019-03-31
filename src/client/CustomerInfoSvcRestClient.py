import requests

def test_rest_api():

    # This test url has already customer id embedded in it.
    apiUrl = "http://0.0.0.0:8000/manage/customer/777/info"

    response = requests.get(apiUrl)
    print(response.content)

if __name__ == '__main__':

    test_rest_api()