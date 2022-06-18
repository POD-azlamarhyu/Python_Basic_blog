import calendar as cal
from calendar import LocaleTextCalendar as ltc

print(cal.month(2000,10))

print(cal.month(2011,3,w=3,l=2))

print(cal.calendar(2001))

ltc_us = ltc(locale='ja_JP')

print(ltc_us.formatmonth(2000,1,1))