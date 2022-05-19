import requests
from dotenv import dotenv_values

ENV = dotenv_values()

query = {
    "lat": '45',
    "lon": '180'
}

response = requests.get(ENV["URL"], params=query)
print(response.json())