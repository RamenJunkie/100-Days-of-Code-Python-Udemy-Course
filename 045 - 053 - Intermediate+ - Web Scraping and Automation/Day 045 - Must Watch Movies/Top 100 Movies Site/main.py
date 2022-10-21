import requests
from bs4 import BeautifulSoup
from datetime import datetime


date = datetime.now().strftime("%Y%m%d")
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
file = date+' - Top100.txt'

# Write your code below this line 👇

page_data = requests.get(url)
#print(page_data.text)

soup = BeautifulSoup(page_data.text, "html.parser")

titles = soup.findAll("h3", class_="title")

for each in reversed(titles):
    #print(each.text)
    with open(file, mode="a",  encoding="utf-8") as writer:
        writer.write(each.text+"\n")

