# TODO 1: Uses Authorization Bearer - Add This
import requests


class SheetyApi:
    from Sheety.sheety_creds import SHEETY_API_KEY

    def __init__(self, api_key=SHEETY_API_KEY):
        self.SHEETY_URL_ENDPOINT = 'https://api.sheety.co/49eca683e8fae67934ccb1bc945f0f89/workout/tracker'
        self.HEADERS = {
            'Authorization': f"Bearer {api_key}",
            'Content-Type': "application/json",
            'Accept': "application/json"
        }

    # TODO 2: CREATE GET:

    def get_sheet_data(self):
        response = requests.get(url=self.SHEETY_URL_ENDPOINT, headers=self.HEADERS)
        return response

    # TODO 3: CREATE POST:

    def post_sheet_data(self, workout_info: dict):
        response = requests.post(url=self.SHEETY_URL_ENDPOINT, headers=self.HEADERS, json=workout_info)
        return response

    # TODO 4: CREATE PUT:

    def put_sheet_data(self, sheet_id: str, workout_info: dict):
        url_endpoint = f"{self.SHEETY_URL_ENDPOINT}/{sheet_id}"
        response = requests.post(url=url_endpoint, headers=self.HEADERS, json=workout_info)
        return response

    # TODO 5: CREATE DELETE:

    def delete_sheet_data(self, sheet_id: str):
        url_endpoint = f"{self.SHEETY_URL_ENDPOINT}/{sheet_id}"
        response = requests.post(url=url_endpoint, headers=self.HEADERS)
        return response


# -------------------------------------------------------------------------------------------------------------------

# get_sheet_data(SHEETY_URL_ENDPOINT, HEADERS)

if __name__ == '__main__':
    post_msg = {
        "tracker": {
            "date": "2023/11/20",
            "time": "15:00:00",
            "exercise": "test_api_post",
            "duration": "60 min",
            "calories": "100",
        }
    }

    put_msg = {
        "tracker": {
            "date": "2023/11/20",
            "time": "15:00:00",
            "exercise": "test_api_put",
            "duration": "60 min",
            "calories": "100",
        }
    }
    print("Testing_Running from sheety_api.py")
    api = SheetyApi()

    print("Testing GET Request")
    get_response = api.get_sheet_data()
    assert get_response.status_code == 200

    print("Testing POST Request")
    post_test = api.post_sheet_data(workout_info=post_msg)
    assert post_test.status_code == 200
    test_id = post_test.json()['tracker']['id']

    print("Testing PUT Request")
    post_test = api.put_sheet_data(sheet_id=test_id, workout_info=put_msg)
    print(post_test.json())
    print("Testing Delete Request")

    delete_test = api.delete_sheet_data(sheet_id=test_id)
    print(delete_test.json())
