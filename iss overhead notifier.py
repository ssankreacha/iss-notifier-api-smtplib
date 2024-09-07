import requests
from datetime import datetime
import smtplib
from tkinter import *

"""
Project Description:

If the ISS (lat, long) is close to my current position (lat, long), and it is currently dark (sunset):
Then send me an email to tell me to look up.
BONUS: run the code every 60 seconds.

How To Test This Code:

Leave program running, sometime in the day when the following criterion are met, then
you should receive an email. 

"""

# Time
window = Tk()

# Current Info
MY_LAT = 0            # TYPE YOUR LAT IN
MY_LONG = 0           # TYPE YOUR LONG IN

# ISS Info
iss_info = requests.get(url="http://api.open-notify.org/iss-now.json")  # api url
iss_info.raise_for_status()     # raise an error based on error code
iss_data = iss_info.json()  # convert into JSON format
iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

# Parameters
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Current Info (API)
my_info = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
my_info.raise_for_status()
my_data = my_info.json()    # converts url info (based off my parameters) into JSON
sunrise = int(my_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(my_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour     # Current time == sunset

on = True
while on:
    window.after(60000)
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:     # Location met
        if time_now >= sunset or time_now <= sunrise:   # Time met, (both) then send email
            sender_email = " "      # Enter your email
            sender_password = " "   # Passkey found with your email provider
            recipient_email = " "   # recipient email

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()  # Secure Connection
                connection.login(user=sender_email, password=sender_password)  # Login
                connection.sendmail(from_addr=sender_email,
                                    to_addrs=recipient_email,
                                    msg="Subject:About Satellite\n\n"f"Hey, Look up!")
                connection.close()  # Closes Connection
