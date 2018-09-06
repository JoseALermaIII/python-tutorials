#! python3
# P05_quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys, shelve, datetime


def getWeather(loc, apikey):
    # Download the JSON data from OpenWeatherMap.org's API.
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' % (loc, apikey)
    response = requests.get(url)
    response.raise_for_status()

    # Load JSON data into a Python variable.
    data = json.loads(response.text)

    now = datetime.datetime.now(tz=datetime.timezone.utc)
    data["savedTime"] = now
    return data


# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: P05_quickWeather.py city,country code')
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
    interval = 10 * 60  # 10 minutes to seconds

    if timedelta.total_seconds() < interval:
        city = weatherShelf["data"]["city"]
        print("RequestError: Need to wait %s minutes. Using saved data for: %s, %s" %
              ((interval - timedelta.total_seconds())/60, city["name"], city["country"]))
    else:
        weatherShelf["data"] = getWeather(location, apiKey)

# Print weather descriptions
w = weatherShelf["data"]['list']
count = int(weatherShelf["data"]["cnt"])

# Print current weather
currentDate = datetime.datetime.strptime(w[0]["dt_txt"][:10], '%Y-%m-%d')
print('Current weather in %s:' % location)
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
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
