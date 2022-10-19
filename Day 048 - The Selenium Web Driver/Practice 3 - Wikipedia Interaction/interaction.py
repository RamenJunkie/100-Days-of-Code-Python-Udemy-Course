

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth import *

url = "https://en.wikipedia.org/wiki/Main_Page"

## Full Path to local Chromedriver.exe file
chrome_driver_path = local_driver

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

num_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
#print(num_articles.get_attribute("href"))
#num_articles.click()

portals = driver.find_element(By.LINK_TEXT, value="Wikibooks")
#portals.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

#search.submit()

driver.find_element(By.LINK_TEXT, value="programming").click()

#driver.quit()