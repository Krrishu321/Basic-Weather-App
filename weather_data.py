import requests

from datetime import datetime

print("Weather Information")

def Show_Weather():
    api_key = "1c80a35b5d27fdde016c76c38891cc97"  # Replace with your API key
    CityName = input("Enter the City Name & Zip Code:-  ")

    weather_data = get_weather(api_key, CityName)
    display_weather(weather_data)
def Time_for_Location (utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def get_weather(api_key, CityName):
    Weather_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': CityName,
        'appid': "1c80a35b5d27fdde016c76c38891cc97",
        'units': 'metric' #faren me convert use
    }

    response = requests.get(Weather_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None
def display_weather(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print(f"\nCurrent Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {temperature}Â°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description.capitalize()}")
        
    else:
        print("Weather data not available.")
Show_Weather()
