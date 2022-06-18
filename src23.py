from datetime import timedelta as td
from datetime import timezone as tz
from datetime import datetime as dt

dt_now = dt.now()
print(dt_now)

print(dt_now.year)
print(dt_now.month)
print(dt_now.day)

print(dt_now.hour)
print(dt_now.minute)
print(dt_now.minute)

date_type = dt_now.date()
print(date_type)

at_date = td(days=1000,seconds=20,minutes=13,hours=1,weeks=10)

print(at_date)
print(dt_now-at_date)
print(dt_now+at_date)
print(dt_now- at_date*4)