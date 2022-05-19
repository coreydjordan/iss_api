import requests
from dotenv import dotenv_values

ENV = dotenv_values()

query = {
    "lat": '45',
    "lon": '180'
}



response = requests.get(ENV["URL"], params=query)
# print(response.json())

latitude = response.json()['iss_position']['latitude']
longitude = response.json()['iss_position']['longitude']

loc_query = {
    "key": ENV["ACCESS_TOKEN"],
    "lon": longitude,
    "lat": latitude,
    "format": "json"
}

loc_res = requests.get(ENV["LOCATION_URL"], params=loc_query)
print(loc_res.json())
# print(longitude,latitude)