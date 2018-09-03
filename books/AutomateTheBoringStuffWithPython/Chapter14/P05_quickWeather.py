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


# datetime.date.fromisoformat implemented in python 3.7,
# though not intended for arbitrary isoformat strings.
# Currently using python 3.6, so change when updated
def dateFromISOformat(datestring):
    year = datestring[:4]
    month = datestring[5:7]
    day = datestring[8:]
    return datetime.date(year=int(year), month=int(month), day=int(day))


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
tomorrowISOdate, dayAfterISOdate = None, None

for i in range(0, count):
    currentISOdate = w[i]["dt_txt"][:10]
    # Print current weather at i == 0
    if i == 0:
        print('Current weather in %s:' % location)
        print(w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description'])
        tomorrowISOdate = str(dateFromISOformat(currentISOdate) + datetime.timedelta(days=1))
        print()
    # If tomorrow date is current date, print tomorrow weather
    elif tomorrowISOdate == currentISOdate:
        print('Tomorrow:')
        print(w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description'])
        dayAfterISOdate = str(dateFromISOformat(currentISOdate) + datetime.timedelta(days=1))
        tomorrowISOdate = None
        print()
    # If day after date is current date, print day after tomorrow weather
    elif dayAfterISOdate == currentISOdate:
        print('Day after tomorrow:')
        print(w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description'])
        break

weatherShelf.close()
