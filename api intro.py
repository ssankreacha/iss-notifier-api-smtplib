import requests
from datetime import datetime
#
MY_LAT = 0
MY_LONG = 0

response = requests.get(url="http://api.open-notify.org/iss-now.json")     # Gets the info from the URL
response.raise_for_status()

data = response.json()      # Retrieve info from API into a JSON format

longitude = data["iss_position"]["longitude"]   # e.g., from the iss_position key, give me longitude info
latitude = data["iss_position"]["latitude"]     # Get hold of the key from the website.

iss_position = (longitude, latitude)
print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0  # 24 hour time
}

time = datetime.now()

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status() # raise an error, the type of error code is important.
sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]
print(sunrise.split("T"))   # This can be split even further.

