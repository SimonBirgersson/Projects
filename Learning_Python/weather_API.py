# Weather API test 220722
import requests

# API key from log in allows us to access the weather data
API_KEY = "fbc90b9b3c31e10d279ca07a08624ae4"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# prompt for entering any city
# city = input("Enter you city: ")
city = "malmö"  # New York"

# create API-request URL
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# fetch URL data
response = requests.get(request_url)

# status code 200 means that connection was succesful
if response.status_code == 200:
    # Convert weather data in JSON format to dict
    data = response.json()

    print(f"Current weather in {data['name']}, {data['sys']['country']}")

    # Get primary description of current weather
    weather = data["weather"][0]["description"]
    print(f"Weather: {weather}")

    # Get current temp in K, convert to °C
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print(f"Temperature: {temperature:.1f}°C")

# status code 400 means connection is unsuccessful
else:
    print(f"An error occured (status code: {response.status_code})")
