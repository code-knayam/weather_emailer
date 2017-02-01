import requests
import datetime

def get_weather_forecast():
    #url to get JSON data with API key and location details

    url = ''
    #generating request
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    #getting key values from JSON data
    city = weather_json['name']
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
    sunrise = get_readable_time( weather_json["sys"]["sunrise"] )
    sunset = get_readable_time( weather_json["sys"]["sunset"] )

    #creating forecast text
    forecast = 'The weather forecast for ' + city + ' today is ' + description
    forecast +=  ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min))
    forecast += ' Sunrise at '  + sunrise
    forecast += ' Sunset at ' + sunset + '\n\n'
    return forecast


def get_readable_time(unix_time):
    #converting UNIX time to local time
    return datetime.datetime.fromtimestamp(int(unix_time)).strftime('%H:%M')
