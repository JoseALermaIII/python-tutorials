# Use the requests module to scrape data from http://weather.gov/.
# Write a program that runs just before you wake up in the morning and checks
# whether it’s raining that day. If so, have the program text you a reminder to pack
# an umbrella before leaving the house.

import requests, bs4, datetime


def get_weather(url_arg):
    # Download url_arg and soupify
    res = requests.get(url_arg)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Parse current weather from soup
    weather_element = soup.select('.myforecast-current')
    return weather_element[0].getText()


def remember_umbrella(weather_arg):
    # Check weather_arg for rain
    tokens = ['rain', 't-storms']

    for token in tokens:
        if token in weather_arg.lower():
            return True
    return False


def check_time(time_arg):
    # Check for time_arg
    time_now = datetime.datetime.now().time()

    if time_now < time_arg:
        print(f'RuntimeError: can\'t run until {time_arg}')
        return False
    return True


def main():
    import time
    from pythontutorials.books.AutomateTheBoringStuff.Ch16.P5_textMyself import textmyself

    # Wait for wake_time
    sleep_time = datetime.timedelta(minutes=5)
    wake_time = datetime.time(hour=5)

    while not check_time(wake_time):
        time.sleep(sleep_time.total_seconds())

    # Get current weather
    url = 'https://forecast.weather.gov/MapClick.php?lat=30.26759000000004&lon=-97.74298999999996'
    weather = get_weather(url)

    # If raining, text cellphone
    if remember_umbrella(weather):
        message = f'Bring an umbrella, there\'s {weather.lower()}'
        textmyself(message)


# If run directly (instead of imported), run main()
if __name__ == '__main__':
    main()
