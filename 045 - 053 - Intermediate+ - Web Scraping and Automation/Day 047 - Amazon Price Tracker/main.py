## Monitors prices on Amazon.com from the items listed in want_list.txt
## want_list.txt should be formtted as url, desired price

import requests
from bs4 import BeautifulSoup
import mailer_class
from time import sleep

url = ""
lowest_price = 0.0
mailer = mailer_class.Mailer()
file = "want_list.txt"

header = {"Accept-Language": "en-US,en;q=0.5",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}


def check_price(url, lowest_price):
    item_data = requests.get(url=url, headers=header)
    item_soup = BeautifulSoup(item_data.text, "lxml")

    item_name = item_soup.find("span", id="productTitle").text
    item_price = float(item_soup.find("span", class_="a-offscreen").text.strip('$'))
    # print(price[1:])

    if item_price < lowest_price:
        message = f"Subject:Price Alert! - {item_name}\n\n{item_name} is at {str(item_price)}\n\nAmazon Link: {url}.\n\n -- Mailer Bot"
        mailer.send_email(message)

# check_price(url,lowest_price)
with open(file) as wants:
    want_list = ((wants.read()).split("\n"))

for each in want_list:
    single = each.split(",")
    single_url = single[0]
    desired_price = float(single[1])
    check_price(single_url,desired_price)
    sleep(60)


