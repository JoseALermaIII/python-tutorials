# This program uses the datetime module to manipulate dates and times.

# The datetime Module
import datetime, time
print(datetime.datetime.now())

dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print((dt.year, dt.month, dt.day))
print((dt.hour, dt.minute, dt.second))

print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
print(halloween2015 == oct31_2015)
print(halloween2015 > newyears2016)
print(newyears2016 > halloween2015)
print(newyears2016 != oct31_2015)
