import requests
from pprint import pprint

API_Key = 'e0d0962e702fa62f8ced14cf6e662d52'
city = ("input city you wanna know weather: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather = requests.get(base_url).json()

pprint(weather)