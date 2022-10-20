
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth import *

url = "http://myhttpheader.com/"

## Full Path to local Chromedriver.exe file
chrome_driver_path = local_driver

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)





