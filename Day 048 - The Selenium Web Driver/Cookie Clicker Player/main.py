## Auto Play Cookie Clicker Game

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth import *
import time

## Old Version
url = "http://orteil.dashnet.org/experiments/cookie/"

## Full Path to local Chromedriver.exe file
chrome_driver_path = local_driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

store={}

def buy_least(money):
    store_raw = driver.find_element(By.ID, value="store").text.split("\n")
    #print(store_raw)
    for each in store_raw:
        if "-" in each:
            split = each.split(" - ")
            if int(split[1].replace(",", "")) < money:
                #print("BUY!")
                driver.find_element(By.ID, value=f"buy{split[0]}").click()

t_end = time.time() + 60 * 5
while True:
    driver.find_element(By.ID, value="cookie").click()
    money = int(driver.find_element(By.ID, value="money").text)
    #print(money)
    buy_least(money)
    if time.time() == t_end:
        print(driver.find_element(By.ID, value="cps").text)

## 50 Cookies per Second then crashed
#driver.quit()