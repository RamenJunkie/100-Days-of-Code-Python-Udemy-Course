## Extract Events from Moment House

import event_class
from bs4 import BeautifulSoup
import requests
import json
import datetime

def fix_date(bad_dates):
    if len(bad_dates) < 5:
        return f"{datetime.datetime.now().year}-{bad_dates}"
    elif bad_dates[4] == "-":
        return bad_dates[0:10]
    else:
        year = datetime.datetime.now().year
        bad_dates = f"{year}-{bad_dates}".replace(" / ", "-")[0:10].replace("/","-")


    return bad_dates

def get_moment_house():
    url = "https://momenthouse.com"
    page_data = requests.get(url)
    #print(page_data.text)

    soup = BeautifulSoup(page_data.text, "html.parser")

    event_json = json.loads(soup.find(id="__NEXT_DATA__").text)

    print(event_json)

    moment_events = []

    for each in event_json['props']['pageProps']['premiereEvents']:
        if "from" not in each['featureInfo']['eventDate']:
            date = fix_date(each['featureInfo']['eventDate'])
            moment_events.append(
                event_class.Event(date, each['displayName'], each['featureInfo']['eventTitle'], "Moment House"))

    return moment_events

