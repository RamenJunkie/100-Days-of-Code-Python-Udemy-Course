## Get Upcoming events on Python.org

from selenium import webdriver
from selenium.webdriver.common.by import By
from auth import *

url = "https://www.python.org"

## Full Path to local Chromedriver.exe file
chrome_driver_path = local_driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

dates = driver.find_elements(By.CLASS_NAME, value= "event-widget time")
events = driver.find_elements(By.CLASS_NAME, value= "event-widget li a")
dates_dict = {}
for item in range(len(dates)):
    dates_dict[item] = {
                       "time": dates[item].text,
                       "event": events[item].text,
                        }

print(dates_dict)
driver.quit()