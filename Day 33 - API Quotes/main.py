import requests
from datetime import datetime

MY_LAT = 37
MY_LONG = -122
MY_TZID = "America/Los_Angeles"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": MY_TZID
}

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

#iss_latitude = float(data["iss_position"]["latitude"])
#iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = MY_LAT
iss_longitude = MY_LONG

dt = datetime.now()
#my_hour = dt.hour
#my_minute = dt.minute

my_hour = 22
my_minute = 15

night_time = False
overhead = False



def look_up():
    print("Lookup")

def compare_iss_loc():
    global overhead
    if iss_latitude > (MY_LAT - 5) and iss_latitude < (MY_LAT + 5):
        if iss_longitude > (MY_LONG - 5) and iss_longitude < (MY_LONG + 5):
            overhead = True

sunset_response = requests.get(" https://api.sunrise-sunset.org/json",params=parameters)
sunset_response.raise_for_status()
my_sun_settings = sunset_response.json()
my_sunset = my_sun_settings["results"]["sunset"]
my_sunrise = my_sun_settings["results"]["sunrise"]
my_sunrise = my_sunrise.split("T")[1].split(":")
my_sunset = my_sunset.split("T")[1].split(":")

if my_hour > int(my_sunset[0]):
    night_time = True
elif my_hour == int(my_sunset[0]):
    if my_minute >= int(my_sunset[1]):
        night_time = True
if my_hour < int(my_sunrise[0]):
    night_time = True
elif my_hour == int(my_sunrise[0]):
    if my_minute <= int(my_sunrise[1]):
        night_time = True

if night_time:
    compare_iss_loc()

print(f"Sunset: {my_sunset}")
print(f"Sunrise: {my_sunrise}")
if overhead == True:
    look_up()
print(night_time)