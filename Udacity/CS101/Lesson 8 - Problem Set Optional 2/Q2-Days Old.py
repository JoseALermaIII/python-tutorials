# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    days = 0
    days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def check_leap_year(year):
        if year % 4 != 0:
            return 0
        if year % 100 != 0:
            return 1
        if year % 400 != 0:
            return 0
        return 1

    def get_days_in_year(year):
        if check_leap_year(year):
            return 366
        return 365

    def get_day_of_year(month, day):
        day_of_year = 0
        i = 0
        while i < month - 1:
            day_of_year += days_of_months[i]
            i += 1
        day_of_year += day  # Adjust for partial month
        return day_of_year

    def get_days_left(year, day_of_year):
        if check_leap_year(year):
            return 366 - day_of_year
        return 365 - day_of_year

    def get_days_between_years(year1_, year2_):
        days_between_years = 0
        i = year1_ + 1
        while i < year2_:
            days_between_years += get_days_in_year(i)
            i += 1
        return days_between_years

    if year1 != year2:
        days = (get_days_left(year1, get_day_of_year(month1, day1))
                + get_days_between_years(year1, year2)
                + get_day_of_year(month2, day2))
    else:
        days = get_day_of_year(month2, day2) - get_day_of_year(month1, day1)

    if check_leap_year(year2) and month2 > 2:
        days += 1

    return days


# Test routine

def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()
