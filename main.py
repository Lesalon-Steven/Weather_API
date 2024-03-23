import requests

api_keys = "2751b832c8d9e4cd189f39b0b8afd99a"
parameters = {
    "lat": 30,
    "lon": 40,
    "appid": api_keys,
    "cnt" : 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
#find the id in the weather data


for data in weather_data["list"]:
    weather_condition = data["weather"][0]["id"]

    if weather_condition > 700:
        print("Bring an umbrella")
    print(weather_condition)

# loop through the weather data and print the weather condition for the next 4 days


# Path: .env
#API_KEY=2751b832c8d9e4cd189f39b0b8afd99a

