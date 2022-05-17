### Day 32 - Email Simple Mail Transfer Protocol and the datetime module - Automated birthday wisher app

### Project - Sending motivational quotes for the week

import datetime as dt
import random
import smtplib

MY_EMAIL = "test@abv.bg"
MY_PASSWORD = "abcd12()"


now = dt.datetime.now()
current_day = now.weekday()
if current_day == 0: #Monday

    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines() #getting the lines as a list
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.abv.bg", port=465) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=f"Subject:Monday motivation\n\n{quote}")