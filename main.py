import requests


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "053a8df930e92e35859269608dafbd10"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


