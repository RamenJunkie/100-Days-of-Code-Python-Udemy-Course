import requests
from auth import *
import datetime

pixela_entpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": pixela_key,
}

user_params = {
    "token": pixela_key,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#Needed to create a user, uncomment and run once.
#response = requests.post(url = pixela_entpoint, json = user_params)
#print(response.text)

graph_endpoint = f"{pixela_entpoint}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding",
    "unit": "Minutes",
    "type": "int",
    "color": "sora"
}


#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

# Post a Pixel
def post_pixel(graph_name, quantity):
    date = datetime.datetime.now().strftime("%Y%m%d")
    pixel_endpoint = f"{pixela_entpoint}/{username}/graphs/{graph_name}"
    pixel_config = {
        "date": date,
        "quantity": str(quantity),
    }
    response = requests.post(url = pixel_endpoint, json=pixel_config, headers = headers)
    print(response.text)

post_pixel("graph1", 60)
## - https://pixe.la/v1/users/ramenjunkie/graphs/graph1.html

## Update  a Pixel
#/v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

