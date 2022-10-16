## Get all URLs on Hackernews

from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

page_data = requests.get(url)
#print(page_data.text)

soup = BeautifulSoup(page_data.text, "html.parser")

all_anchors = soup.findAll("span", "titleline")
for tag in all_anchors:
    print(tag.a.text)
    print(tag.a['href'])


