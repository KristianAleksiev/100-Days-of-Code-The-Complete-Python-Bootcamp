import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL = "test@abv.bg"
MY_PASSWORD = "abcd12()"

#Looking for a match
today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

#Comprehending the dictionary
birthday_dictionary = {(data_row["month"], data_row["day"]):data.row for (index, data_row) in data.iterrows()}
if today in birthday_dictionary:
    birthday_person = birthday_dictionary[today]
    letter_template = random.randint(1, 3)
    file_path = f"letter_templates/letter_{letter_template}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"]) ### Replace the value, bug fixed
    #Sending the mail
    with smtplib.SMTP("smtp.abv.bg", port=465) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")

### Pythonanywhere.com cloud hosting, Running the code every day
# $ python3 automated_birthday_wisher.py #Authentication error, getting access
#Setting a scheduled task at a desired time

