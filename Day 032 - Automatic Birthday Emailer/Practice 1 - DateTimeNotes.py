import datetime as dt

print(dt.datetime.now().year)
print(dt.datetime.now().month)
print(dt.datetime.now().day)
print(dt.datetime.now().hour)
print(dt.datetime.now().minute)
print(dt.datetime.now().second)
print(dt.datetime.now().weekday())

date_of_birth = dt.datetime(year = 1979, month = 12, day = 23, hour = 2, minute = 14)

print(date_of_birth)

if dt.datetime.now().weekday() == 0:
    print("It's Monday")
elif dt.datetime.now().weekday() == 2:
    print("It's Wednesday My Dudes!")


