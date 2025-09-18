import requests
from data import *
from twilio.rest import Client

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid":MY_API_KEY,
    "cnt": FORECAST_TO_CHECK
}

def send_rain_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_TOKEN)
    message = client.messages.create(
        body="Bring an Umbrella, its going to rain",
        from_="+18889923071",
        to="+14082035064"
    )

request = requests.get(url=WEATHER_API_URL,params=parameters)
request.raise_for_status()
weather_data = request.json()
print(weather_data)
bring_umbrella = False
for grouping in weather_data["list"]:
    print(grouping["weather"])
    if grouping["weather"][0]["id"] < 700:
        bring_umbrella = True


if bring_umbrella == True:
    send_rain_sms()





