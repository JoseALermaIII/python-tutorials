#! python3
# P05_quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys, shelve, datetime, copy


def getWeather(shelf, loc, apikey):
    # Download the JSON data from OpenWeatherMap.org's API.
    url = 'http://api.openweathermap.org/data/2.5/forecast?id=%s&APPID=%s' % (loc, apikey)
    response = requests.get(url)
    response.raise_for_status()

    # Load JSON data into a Python variable.
    data = json.loads(response.text)

    # Save Data
    shelf = copy.deepcopy(data)

    timeNow = datetime.datetime.now(tz=datetime.timezone.utc)
    shelf["savedTime"] = timeNow
    shelf.close()
    return data


def getLocationID(loc):
    # TODO: download and parse city list
    return cityID


# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: P05_quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# TODO: Convert location to location ID
locID = getLocationID(location)

# Get API Key from file
with open("apikey.txt") as file:
    key = file.read()

# Open shelf to read data
weatherShelf = shelve.open("weather", 'c')

# Download and save data to shelf
if not list(weatherShelf.keys()):  # Shelf empty, download data
    weatherData = getWeather(weatherShelf, locID, key)
else:
    # Check for 10 minute interval between API requests
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    savedTime = weatherShelf["savedTime"]
    timedelta = now - savedTime
    interval = 10 * 60  # 10 minutes to seconds

    if timedelta.total_seconds() < interval:
        print("RequestError: Need to wait %s minutes. Using saved data" % ((interval - timedelta)/60))
        weatherData = copy.deepcopy(weatherShelf)
        weatherShelf.close()
    else:
        weatherData = getWeather(weatherShelf, locID, key)

# Print weather descriptions
w = weatherData['list']
print('Current weather in %s:' % location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
