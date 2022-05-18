### Tracking the International Space Station project

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 42.01667
MY_LON = 23.094740
MY_EMAIL = "anon@gmail.com"
MY_PASS = "anonpassword"


def is_iss_near():
    response = requests.get(url="https://api.sunrise-sunset.org/json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LON - 5 <= iss_longitude <= MY_LON +5:
        return True


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0,

    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # Comparing formatting
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60) #Executing every 60 seconds
    if is_iss_near() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:See the ISS\n\nThe ISS is above in the sky, look up"
        )