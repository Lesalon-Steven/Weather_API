import os
import requests
from twilio.rest import Client

account_sid = 'ACcd467830a22b7863dfd5b105731dc707'
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)



api_keys = "2751b832c8d9e4cd189f39b0b8afd99a"
parameters = {
    "lat": 30,
    "lon": 40,
    "appid": api_keys,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
# find the id in the weather data


for data in weather_data["list"]:
    weather_condition = data["weather"][0]["id"]

    if weather_condition > 700:
        message = client.messages.create(
            from_='+13158256361',
            body='bring an umbrella!',
            to='+36208097960'
        )
        print(message.status)
    print(weather_condition)

# loop through the weather data and print the weather condition for the next 4 days


# Path: .env
# API_KEY=2751b832c8d9e4cd189f39b0b8afd99a
