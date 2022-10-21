from auth import *
import requests
import datetime as dt

## User Information
GENDER = "male"
BIRTH_YEAR = 1980  #79 but at the end so I am just fudging this to not deal with months.
WEIGHT = 100  #kgs
HEIGHT = 178  #cms
age = dt.datetime.now().year - BIRTH_YEAR

HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

def get_data():
    exer_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

    user_string = input("What kind of work out did you do today? ")
    #debug user_string = "I swam 50 miles and then biked for 90 minutes and then jumped rope for three hours"
    exer_body = {
        "query": user_string,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": age,
    }

    nutr_reply = requests.post(url = exer_endpoint, json = exer_body, headers=HEADER)
    return nutr_reply.json()

def post_data(item):
    date = dt.datetime.now().strftime("%Y-%m-%d")
    time = dt.datetime.now().strftime("%H:%M:%S")

    sheet_api = "https://api.sheety.co/c9137e520d7bf19bec41b391deb961c7/myWorkouts/workouts"
    sheet_data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"]
        }
    }

    # print(each["name"].title())
    # print(each["duration_min"])
    # print(each["nf_calories"])

    token_header = { "Authorization": "Bearer " +sheety_token}


    reply = requests.post(sheet_api, json = sheet_data, headers= token_header)
    #print(reply.text)

data = get_data()

for each in data["exercises"]:
    post_data(each)



