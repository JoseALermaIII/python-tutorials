"""Remember umbrella

Use :py:mod:`requests` to scrape data from http://weather.gov/.

Write a program that runs just before you wake up in the morning and checks
whether it’s raining that day. If so, have the program text you a reminder to pack
an umbrella before leaving the house.

"""

import requests, bs4, datetime


def get_weather(url_arg: str) -> str:
    """Get weather

    Uses :py:mod:`requests` to download given weather page url, then uses :py:mod:`bs4` to get
    the current weather data text.

    Args:
        url_arg: String containing url to specified city's http://weather.gov/ weather page.

    Returns:
        String with current weather data text.
    """
    # Download url_arg and soupify
    res = requests.get(url_arg)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Parse current weather from soup
    weather_element = soup.select('.myforecast-current')
    return weather_element[0].getText()


def remember_umbrella(weather_arg: str) -> bool:
    """Remember umbrella

    Checks current weather data text from :meth:`get_weather` for keywords indicating rain.

    Args:
        weather_arg: String containing current weather text of specified city.

    Returns:
        True if any of the rain keywords are found, False otherwise.

    """
    # Check weather_arg for rain
    tokens = ['rain', 't-storms']
    """list: Strings of keywords that indicate rain."""

    weather_arg = weather_arg.lower()  # To match tokens' case

    for token in tokens:
        if token in weather_arg:
            return True
    return False


def check_time(time_arg: datetime.time) -> bool:
    """Check time

    Checks if given time is after current time as given by :meth:`datetime.datetime.now`.

    Args:
        time_arg: :class:`datetime.time` object to compare with current time.

    Returns:
        True if given time is after current time.
    """
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
