### Day 35 - API Keys, Authentication, Environment variables and Sending SMS

## API Key - API providers authorising their data usage

import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "26cfd39a725fb906de536a840f7d30a1"
#Twilio id
account_sid = "AC7c357bb2c70d78979800071781270f39"
auth_token = "0549b71f9a1e07f77368c2e0bac53485"


params = {
    "lat": 42.022491,
    "lon": 23.094740,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url=OWM_ENDPOINT, params=params)
response.raise_for_status()
weather_data = response.json()
# code = weather_data["hourly"][0]["weather"][0]["id"]
weather_slice = weather_data["hourly"][:12] #Only 12 hours

will_rain = False

for hour_data in weather_slice:
    condition_id = hour_data["weather"][0]["id"]
    if int(condition_id) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["http_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages.create(
        body="It's raining today. Take an umbrella with you or better - your car 🤭",
        from_="+359886554828",
        to="+359884322566"
    )
    print(message.status)


###Set up the proxy above /\ /// Connection problem
### Pythonanywhere.com setup for sending every morning
## $ python3 day_35_api_keys.py