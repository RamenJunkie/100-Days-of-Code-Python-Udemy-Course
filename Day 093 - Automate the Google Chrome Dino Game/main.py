
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth import *

url = ""

options = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
chrome_driver_path = local_driver

driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
driver.get(url)




driver.quit()