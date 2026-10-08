# exercise to check whether a given date is passed or not
import datetime

target_datetime = datetime.datetime(2025,1,2, 12,15,50)
current_datetime = datetime.datetime.now()

if current_datetime > target_datetime:
    print("Target date has passed")
else:
    print("target date has not passed")