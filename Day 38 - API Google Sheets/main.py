import requests
import datetime as dt

NURTIX_API_KEY = "758f933f701246f2aef95aa4c7aecd04"
NUTRIX_APP_ID = "bcfb6bb8"
NUTRIX_EXERCISE_ENPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
#
# NUTRIX_HEADERS = {
#     "x-app-id": NUTRIX_APP_ID,
#     "x-app-key": NURTIX_API_KEY
# }
#
# query= { "query": "swam for 1 hour"}
#
# response = requests.post(url=NUTRIX_EXERCISE_ENPOINT,headers=NUTRIX_HEADERS,json=query)
# print(response.text)
# workoutData = response.json()
#
# SHEETY_URL = "https://api.sheety.co/76a4a50ca22a6b97fc456fa5be2d0a2a/workoutApiTesting/sheet1"
# date = dt.datetime.now().strftime("%d/%m/%Y")
# time = dt.datetime.now().strftime("%X")
#
sheety_header = {
    "Authorization": "Bearer abbeychase99*"
}
#
# #print(date)
# #print(time)
# #exercise = workout_data["exercises"][0]["name"].title()
# #duration = workout_data["exercises"][0]["duration_min"]
# #calories= workout_data["exercises"][0]["nf_calories"]
# #print(f"I was {exercise} for {duration} minutes expending {calories} calories")
#
# for exercise in workoutData["exercises"]:
#     exercise_data = {
#         "sheet1": {
#             "Date": date,
#             "Time": time,
#             "Exercise": exercise["name"].title(),
#             "Duration": exercise["duration_min"],
#             "Calories": exercise["nf_calories"]
#         }
#     }
#     print(exercise_data)
#
#
#
#     sheety_response = requests.post(url=SHEETY_URL,headers=sheety_header,json=exercise_data)
#     print(sheety_response.text)

import requests
from datetime import datetime


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/76a4a50ca22a6b97fc456fa5be2d0a2a/workoutApiTesting/sheet1"

exercise_text = "swam for 1 hour" #input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRIX_APP_ID,
    "x-app-key": NURTIX_API_KEY,
}

parameters = {
    "query": exercise_text,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=sheety_header)

    print(sheet_response.text)