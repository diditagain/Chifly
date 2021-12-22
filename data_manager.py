import requests
from dotenv import load_dotenv
import os
import json 


load_dotenv()


class DataManager:
    
    SHEETY_API = os.getenv("SHEETY_ENDPOINT")   
    
    def __init__(self, destination_data):
        self.destination_data = {}
        
        
    def get_data(self):
        r = requests.get(url=self.SHEETY_API)
        self.destination_data = r.json()["prices"]
        with open("data/full_data.json", "w") as full_data:
            json.dump(self.destination_data, full_data)
        cities = []
        for locations in self.destination_data:
            city = locations["city"]
            cities.append(city)
        return cities
    
    def put_data(self, id, code):
        edit_data = {
            "price": {
                "iataCode": str(code),
            }
        }
        r = requests.put(url=f"{self.SHEETY_API}/{id}", json=edit_data)
        r.raise_for_status()
