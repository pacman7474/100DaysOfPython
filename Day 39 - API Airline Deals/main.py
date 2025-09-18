#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData



data = DataManager()
search_flight = FlightSearch()

sheet_data = data.get_sheet_data().json()
missing_IATA = False
for deal in sheet_data["deals"]:
    #print(deal)
    if deal["iataCode"] == "":
        deal["iataCode"] = airport_code = search_flight.get_iata_code(deal["city"])
        put_data = {
            "deal": deal
        }
        data.update_sheet_data(put_data)
        #print(put_data)
    offers = FlightData(search_flight.get_flight_offers(deal))
    offers.find_cheapest_flight()
#print(sheet_data)


