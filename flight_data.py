from types import CoroutineType
from dotenv.main import load_dotenv
import requests
import os
import json

load_dotenv()

class FlightData:

    ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
    HEADER = {
        "apiKey": os.getenv("TEQUILA_APIKEY")
    }
    

    def __init__(self, city):
        self.city = city

    def find_code(self):
        city_codes = []
        parameters = {
            "term": self.city
        }
        response = requests.get(url=self.ENDPOINT, headers=self.HEADER, params=parameters)
        response.raise_for_status()
        print(response)
        city_data = response.json()
        print(city_data)
        code = city_data["locations"][0]["code"]
        city_codes.append(code)
        with open("data/city_list.json", "w") as city_list:
            json.dump(city_codes, city_list)
        return code

