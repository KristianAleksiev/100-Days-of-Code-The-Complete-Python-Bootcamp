### Day 37 - Advanced authentication and POST/PUT/DELETE Requests

## HTTP POST requests
# We are giving the external system data, not interested if the response is successful

## PUT request
# Update data

import requests
from datetime import datetime


pixela_endpoint = "https:/pixe.la/v1/users"
TOKEN = "afgtq13mq222mgaimv22ivcaocz"
USERNAME = "Kristian"
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params) #Create user
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "My coding graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora",

}
### Safer authentication with X-USER-TOKEN HEADER- No api key visible
header = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=header)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_config = {
    "date": "20220521", #datetime.now().strftime("%Y%m%d")
    "quantity": "3.5",
}
post_response = requests.post(url=post_endpoint, json=post_config, headers=header)

# Automating the "date" key formatting
#today = datetime.now().strftime("%Y%m%d") ### datetime(year=,month=,day=)

## PUT and DELETE methods

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{post_config['date']}"
put_config = {
    "quantity": "4.5",
}

put_request = requests.put(url=put_endpoint, json=put_config, headers=header)
