### Day 33 - Application programming interfaces - API Endpoints, API Parameters - ISS Tracker

## API - A set of commands, functions, protocols and objects that
## programmers use to create software or interact with an external system

## API Endpoint - URL
# import requests
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# #response codes - 1xx - Informational, 2xx - success, 3xx - redirection, 4xx- user error, 5xx - server error
# print(response.status_code)
# response.raise_for_status() # Raises exception with the error code
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

## API parameters - Required or Optional(devault value)
import requests
from datetime import datetime
MY_LAT = 42.01667
MY_LON = 23.094740

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0,

}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) #Comparing formatting
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour
