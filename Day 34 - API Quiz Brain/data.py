import requests
import html

OPEN_TRIVIA_URL = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18
}

response = requests.get(OPEN_TRIVIA_URL, params=parameters)
response.raise_for_status()
response_data = response.json()
question_data = response_data["results"]

