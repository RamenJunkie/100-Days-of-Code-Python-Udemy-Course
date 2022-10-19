## Sign up for App Prewery Newsletter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth import *

url = "https://secure-retreat-92358.herokuapp.com"

## Full Path to local Chromedriver.exe file
chrome_driver_path = local_driver

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

form_entry = driver.find_element(By.NAME, value="fName")
form_entry.send_keys("FIRST")
form_entry = driver.find_element(By.NAME, value="lName")
form_entry.send_keys("LASt")
form_entry = driver.find_element(By.NAME, value="email")
form_entry.send_keys("EMAIL HERE")
driver.find_element(By.CSS_SELECTOR, value="button").click()


#driver.quit()