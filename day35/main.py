import requests

OWN_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "e70f0abd49a8988586333e110b6c1555"

parameters = {
    "lat": 35.689198,
    "long": 51.388973,
    "appid": api_key,
}


response = requests.get(OWN_ENDPOINT, params=parameters)
data = response.json()