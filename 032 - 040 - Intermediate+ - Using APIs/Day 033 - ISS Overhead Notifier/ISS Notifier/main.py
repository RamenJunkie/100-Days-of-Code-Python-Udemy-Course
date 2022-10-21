import requests
import datetime as dt
import mailer_class

email = "josh_miller79@outlook.com"
mailer = mailer_class.Mailer()

def iss_close(iss_cord, my_cord):
    #DEBUG iss_cord = my_cord
    if int(iss_cord[0]) in range(int(my_cord[0])-5,int(my_cord[0])+5) and int(iss_cord[1]) in range(int(my_cord[1])-5,int(my_cord[1])+5):
        return True

def get_iss():
    iss_loc = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_loc.raise_for_status()
    iss_data = iss_loc.json()
    longitude = iss_data["iss_position"]["longitude"]
    latitude = iss_data["iss_position"]["latitude"]
    return (latitude,longitude)

def get_sunrise(pos):
    sunrise = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={pos[0]}&lng={pos[1]}&formatted=0")
    sunrise.raise_for_status()
    sun_data = sunrise.json()
    #DEBUG print(sun_data)
    sunset = int(((sun_data["results"]["sunset"].split("T"))[1]).split(":")[0])
    sunrise = int(((sun_data["results"]["sunrise"].split("T"))[1]).split(":")[0])
    return (sunrise,sunset)

timespan = get_sunrise(my_lat_lon)
iss_lat_lon = get_iss()
time = dt.datetime.now().hour

if time <= timespan[0] or time >= timespan[1]:
    if iss_close(iss_lat_lon, my_lat_lon):
        mailer.send_email(email, "Subject:ISS Notifier\n\nThe ISS should be visible in your area overhead!\n\n -- Notifier Bot")

