import datetime

now=datetime.datetime.now()

print("current date time ")

print(now.strftime("DATE=>%d-%m-%y \nTIME=>%H %M %S" ))