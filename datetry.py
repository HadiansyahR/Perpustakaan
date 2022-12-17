import datetime as dt

today = dt.date.today()
nextday = today + dt.timedelta(days=29)
d1 = today.strftime("%Y-%m-%d")

print(d1)
print(nextday)
