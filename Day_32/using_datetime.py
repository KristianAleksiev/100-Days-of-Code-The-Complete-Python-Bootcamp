### Datetime module

import datetime as dt

now = dt.datetime.now() # Current date and time
year = now.year #Int
month = now.month
day_of_week = now.weekday() #Returns a number

date_of_birth = dt.datetime(year=1995, month=12, day=15) #00:00 as default time, could change if needed
