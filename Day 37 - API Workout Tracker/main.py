import requests
import datetime as dt

pixela_endpoint_user = "https://pixe.la/v1/users"


USERNAME = "pacman7474"
TOKEN = "dfkjfo49fsxv39v8Df49"

pixela_parameters = {
    "token": "dfkjfo49fsxv39v8Df49",
    "username": "pacman7474",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint,json=pixela_parameters)
#response.raise_for_status()

pixela_endpoint_create_graph = f"{pixela_endpoint_user}/{USERNAME}/graphs"

graph_config = {
    "id": "exercise1",
    "name": "Pelaton Graph",
    "unit": "miles",
    "type": "float",
    "color": "ajisai"
}

header_token = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=pixela_endpoint_create_graph,json=graph_config,headers=header_token)
#print(response.text)

today=dt.datetime.now().strftime("%Y%m%d")

pixel_add = {
    "date": today,
    "quantity": "5.2"
}

# response = requests.post(f"{pixela_endpoint_create_graph}/{graph_config['id']}",json=pixel_add,headers=header_token)
# response.raise_for_status()

pixel_update = {
    "date": today,
    "quantity": "10"
}

# response = requests.put(f"{pixela_endpoint_create_graph}/{graph_config['id']}/{today}",json=pixel_update,headers=header_token)
# response.raise_for_status()

response = requests.delete(url=f"{pixela_endpoint_create_graph}/{graph_config['id']}/{today}",headers=header_token)
response.raise_for_status()