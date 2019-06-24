# import datetime

import datetime as dt

today = dt.datetime.today()
print("Its:",today)

tomorrow = dt.datetime(2019, 6, 25, 12, 45, 33, 12)
print("Tomorrow is:",tomorrow)

howManyDays = tomorrow - today
print("How Many Days: ",howManyDays)