import datetime
date = datetime.date(2025,1,2) #(year, month, day)
aaj = datetime.date.today()
print(aaj)

time = datetime.time(12,30,0) #(hour, minute, second)
abhi = datetime.datetime.now()

abhi = abhi.strftime("%H:%M:%S %d - %m - %y") #it is a format specifier

print(abhi)