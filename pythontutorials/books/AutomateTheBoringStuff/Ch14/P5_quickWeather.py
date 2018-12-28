#! python3
"""Quick weather

Prints 3-day weather information for a location specified in the command line.

"""

import json, requests, sys, shelve, datetime


def getWeather(loc: str, apikey: str) -> dict:
    """Get weather

    Uses `OpenWeatherMap.org`_ API to get JSON data of given location with given API key. Data is stored as a
    :class:`dict` and the current date and time (in UTC) is also stored using :meth:`datetime.datetime.now`.

    Args:
        loc: Location to get weather data of in ``City,Country Code`` format.
        apikey: API key used to interface with `OpenWeatherMap.org`_'s API.

    Returns:
        Dictionary with weather JSON data and current date time (in UTC) added.

    .. _OpenWeatherMap.org:
        https://openweathermap.org/api
        
    """
    # Download the JSON data from OpenWeatherMap.org's API.
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' % (loc, apikey)
    response = requests.get(url)
    response.raise_for_status()

    # Load JSON data into a Python variable.
    data = json.loads(response.text)

    now = datetime.datetime.now(tz=datetime.timezone.utc)
    data["savedTime"] = now
    return data


def main() -> None:
    """P5_quickWeather.py

    Displays given location's 3-day weather information.

    Returns:
        None. Weather data is printed to terminal and JSON data is stored in a :py:mod:`shelve` shelf, ``weather``.

    Note:
        To prevent excessive API requests, JSON data is stored in a :py:mod:`shelve` shelf and only redownloaded every
        10 minutes. Time is kept track using :meth:`datetime.datetime.now` and :class:`datetime.timedelta`.

    """
    # Compute location from command line arguments.
    if len(sys.argv) < 2:
        print('Usage: P5_quickWeather.py city,country code')
        sys.exit()
    location = ' '.join(sys.argv[1:])
    
    # Get API Key from file
    with open("apikey.txt") as file:
        apiKey = file.read()
    
    # Open shelf to read data
    weatherShelf = shelve.open("weather")
    
    # Download and save data to shelf
    if not list(weatherShelf.keys()):  # Shelf empty, download data
        weatherShelf["data"] = getWeather(location, apiKey)
    else:
        # Check for 10 minute interval between API requests
        timeNow = datetime.datetime.now(tz=datetime.timezone.utc)
        savedTime = weatherShelf["data"]["savedTime"]
        timedelta = timeNow - savedTime
        interval = datetime.timedelta(minutes=10)
    
        if timedelta < interval:
            city = weatherShelf["data"]["city"]
            print("RequestError: Need to wait %s minutes. Using saved data for: %s, %s" %
                  (round((interval - timedelta).total_seconds()/60, 2), city["name"], city["country"]))
        else:
            weatherShelf["data"] = getWeather(location, apiKey)
    
    # Print weather descriptions
    w = weatherShelf["data"]['list']
    count = int(weatherShelf["data"]["cnt"])
    
    # Print current weather
    print('Current weather in %s:' % location)
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    currentDate = datetime.datetime.strptime(w[0]["dt_txt"][:10], '%Y-%m-%d')
    tomorrowDate = currentDate + datetime.timedelta(days=1)
    dayAfterDate = currentDate + datetime.timedelta(days=2)
    print()
    
    for i in range(1, count):
        currentDate = datetime.datetime.strptime(w[i]["dt_txt"][:10], '%Y-%m-%d')
        # If current date is greater than tomorrow date, print tomorrow weather
        if currentDate > tomorrowDate:
            print('Tomorrow:')
            print(w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description'])
            tomorrowDate = currentDate + datetime.timedelta(days=7)  # past the 5-day forecast
            print()
        # If current date is greater than day after date, print day after tomorrow weather
        elif currentDate > dayAfterDate:
            print('Day after tomorrow:')
            print(w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description'])
            break
    
    weatherShelf.close()


if __name__ == '__main__':
    main()
