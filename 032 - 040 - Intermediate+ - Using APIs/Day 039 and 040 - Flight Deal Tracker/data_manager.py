import requests
from auth import *

class DataManager:

    def __init__(self):
        self.sheet_api = "https://api.sheety.co/c9137e520d7bf19bec41b391deb961c7/flightDeals/prices"
        self.token_header = {"Authorization": "Bearer " + sheety_token}
        self.get_data()


    def add_city(self, item):
        sheet_data = {
            "price": {
                "city": "Test4",
                "iataCode": "CODE",
                "lowestPrice": "50",
            }
        }

        reply = requests.post(self.sheet_api, json=sheet_data, headers=self.token_header)

    def get_data(self):
        response = requests.get(url=self.sheet_api, headers = self.token_header)
        self.data = response.json()

    def add_code(self, city, row):
        # Not pulling real codes because lack of API, but it would be a Get based onbn city.
        fake_code = city[0:3].upper()

        put_data = {
            "price": {
                "iataCode": fake_code
            }
        }

        reply = requests.put(self.sheet_api+"/"+str(row), json=put_data, headers=self.token_header)
        print(reply)



