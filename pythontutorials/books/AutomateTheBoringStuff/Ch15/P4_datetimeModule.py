"""datetime module

This program uses :py:mod:`datetime` to manipulate dates and times.

"""


def main():
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

    # The timedelta Data Type
    delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
    print((delta.days, delta.seconds, delta.microseconds))
    print(delta.total_seconds())
    print(str(delta))

    dt = datetime.datetime.now()
    print(dt)
    thousandDays = datetime.timedelta(days=1000)
    print(dt + thousandDays)

    oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
    aboutThirtyYears = datetime.timedelta(days=365 * 30)
    print(oct21st)
    print(oct21st - aboutThirtyYears)
    print(oct21st - (2 * aboutThirtyYears))

    # Pausing Until a Specific Date
    halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
    while datetime.datetime.now() < halloween2016:
        time.sleep(1)

    # Converting datetime Objects into Strings
    print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
    print(oct21st.strftime('%I:%M %p'))
    print(oct21st.strftime("%B of '%y"))

    # Converting Strings into datetime Objects
    print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
    print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
    print(datetime.datetime.strptime("October of '15", "%B of '%y"))
    print(datetime.datetime.strptime("November of '63", "%B of '%y"))


if __name__ == '__main__':
    main()
