from datetime import time
import os
from dotenv import load_dotenv
from dotenv.main import set_key
import requests

load_dotenv()

class FlightSearch:
    ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
    HEADER = {
        "apiKey": os.getenv("TEQUILA_APIKEY")
    }

    def __init__(self, date_from, date_to) -> None:
        self.city_from = "city:ADA"
        self.date_from = date_from
        self.date_to = date_to
        self.market = "TR"
    def search_flights(self, city_to):
        parameters = {
            "fly_from": self.city_from,
            "fly_to": city_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "partner_market": self.market,
            "curr": "TRY"
        }
        response = requests.get(url=self.ENDPOINT, headers=self.HEADER, params=parameters).json()
        print(response)
        price = response["data"][0]["price"]
        time = response["data"][0]["local_departure"]
        return price, time

    
