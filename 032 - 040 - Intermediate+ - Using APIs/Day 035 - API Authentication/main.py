## https://www.weatherapi.com/api-explorer.aspx

## This one feels a bit sloppy but it does the job.  OpenWeatherMap wants a payment method
## so used an alternative, Twilio just suspended my account for some reason but sms works
## directly though Phone# @ txt.att.com.

from auth import *
import requests
import mailer_class

weather = requests.get(url=f"http://api.weatherapi.com/v1/forecast.json?q={zip}&key={appid}")
weather.raise_for_status()
weather_data = weather.json()
mailer= mailer_class.Mailer()

twelve_hour = []
for each in range(0,12):
    twelve_hour.append(weather_data["forecast"]["forecastday"][0]["hour"][each]["condition"]["text"])

rain_cond = ["Patchy rain possible", "Thundery outbreaks possible","Patchy light drizzle","Light drizzle",
             "Patchy light rain","Light rain","Moderate rain at times","Moderate rain","Heavy rain at times",
             "Heavy rain","Light rain shower", "Patchy light rain with thunder","Moderate or heavy rain with thunder",
             "Moderate or heavy rain shower","Torrential rain shower"]
snow_cond = ["Patchy snow possible","Patchy sleet possible","Patchy freezing drizzle possible", "Blowing snow",
             "Blizzard","Freezing drizzle","Heavy freezing drizzle", "Light freezing rain",
             "Moderate or heavy freezing rain","Light sleet", "Moderate or heavy sleet","Patchy light snow",
             "Light snow", "Patchy moderate snow","Moderate snow", "Patchy heavy snow","Heavy snow",
             "Light snow showers","Moderate or heavy snow showers"]

rain = False

for each in twelve_hour:
    if each in rain_cond:
        rain = True

if rain:
    message = "Subject: Rainy Weather Notice!\n\nLooks like rain later today, better take an umbrella.\n\n - Mailer Bot"
    mailer.send_email(message)