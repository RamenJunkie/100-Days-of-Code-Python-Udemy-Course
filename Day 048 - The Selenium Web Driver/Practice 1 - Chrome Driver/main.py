from selenium import webdriver
from selenium.webdriver.common.by import By
from auth import *

## Full Path to local Chromedriver.exe file
chrome_driver_path = local_driver

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/Star-Wars-SW-SAN-Francisco/dp/B09H1GJX9B/")
# price = driver.find_element(By.ID,value="priceblock_ourprice")
# print(price.text)
#
# driver.close()

driver.get("https://www.python.org")
# seachbar = driver.find_element(by="name", value="q")
# print(seachbar.tag_name)
# print(seachbar.get_attribute("placeholder"))
# logo = driver.find_element(By.CLASS_NAME, value="python-logo")
# print(logo.size)
# print(logo.tag_name)
#
# doc_link = driver.find_element(By.CSS_SELECTOR, value = ".documentation-widget a")
# print(doc_link.text)
#
# submit_link = driver.find_element(By.XPATH, value='/html/body/div/footer/div[1]/div/ul/li[7]/ul/li[5]/a')
# print(submit_link.text)

driver.find_elements()

## Closes one tab
#driver.close()
## Closes all instances
driver.quit()