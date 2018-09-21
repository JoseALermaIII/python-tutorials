# Use the requests module to scrape data from http://weather.gov/.
# Write a program that runs just before you wake up in the morning and checks
# whether it’s raining that day. If so, have the program text you a reminder to pack
# an umbrella before leaving the house.

import requests, bs4, datetime
from books.AutomateTheBoringStuffWithPython.Chapter16.P05_textMyself import textmyself


def check_time(time_arg):
    # Check for wake time
    time_now = datetime.datetime.now().time()

    if time_now < time_arg:
        print(f'RuntimeError: can\'t run until {time_arg}')
        return False
    return True


def remember_umbrella():
    # Download weather url and soupify
    url = 'https://forecast.weather.gov/MapClick.php?lat=30.26759000000004&lon=-97.74298999999996'

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Parse current weather from soup
    weather_element = soup.select('.myforecast-current')
    weather = weather_element[0].getText()

    # If raining, text cellphone
    tokens = ['rain', 't-storms']

    for token in tokens:
        if token in weather.lower():
            message = f'Bring an umbrella, there\'s {weather.lower()}'
            textmyself(message)
    return None


# If run directly (instead of imported) wait for wake time, then run
if __name__ == '__main__':
    import time

    sleep_time = datetime.timedelta(minutes=5)
    wake_time = datetime.time(hour=5)
    while not check_time(wake_time):
        time.sleep(sleep_time.total_seconds())
    remember_umbrella()
