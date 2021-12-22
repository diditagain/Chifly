from data_manager import DataManager as dm
from flight_data import FlightData  as fd
from flight_search import FlightSearch as fs
from notification_manager import NotificationManager as nm
import json
import datetime as dt



data_manager = dm({})
cities_data = data_manager.get_data()




# id = 2
# for city in cities_data:
#     city_name = city
#     print(city_name)
#     city = fd(city_name)
#     city_code = city.find_code()
#     print(city_code)
#     data_manager.put_data(id=id, code=city_code)
#     id += 1

# updated_data = data_manager.get_data()

with open("data/full_data.json", "r") as data:
    updated_data = json.load(data)

    
date = dt.datetime.now()
date2 = date + dt.timedelta(days=30)

date_from = date.strftime("%d/%m/%Y")
date_to = date2.strftime("%d/%m/%Y")

flight_info = fs(date_from=date_from, date_to=date_to)

for destinations in updated_data:
    print(destinations)
    iata_code = destinations["iataCode"]
    print(iata_code)
    code = f"city:{iata_code}" 
    price = destinations["lowestPrice"]
    city = destinations["city"]
    result = flight_info.search_flights(code)
    if int(result[0]) < price:
        time = result[1]
        price = result[0]
        message = f"A flight to {city} at {time} is {price} TL. Cheaper than you expected!"
        nm().send_mail(message=message)
    else:
        pass


    
