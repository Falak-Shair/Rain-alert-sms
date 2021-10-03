import requests
import os
from twilio.rest import Client

api_key = os.environ.get("API_KEY")
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACb19b2054a0a3fbc5732431560d8bd4ea"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 24.860735,
    "lon": 67.001137,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_data = hour_data['weather'][0]['id']
    if condition_data < 700:
        will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an umbrella. ☂ ",
        from_='+12183877347',
        to='+923402822957'
    )

    print(message.status)
