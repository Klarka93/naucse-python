import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 50.0755,
    "longitude": 14.4378,
    "current_weather": True
}

response = requests.get(url, params=params)
data = response.json()

print(data["current_weather"])
