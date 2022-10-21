
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth import *
import requests
from bs4 import BeautifulSoup
from time import sleep

url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
file = "zillow.html"

## Full Path to local Chromedriver.exe file
chrome_driver_path = local_driver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

##### DRIVER PORTION WORKS BUT ZILLOW THINKS I AM A BOT SO REPLACED WITH TEXT VERSION OF THE PAGE. #####
#driver.get(url)


#for _ in range(20):
#    webdriver.ActionChains(driver).key_down(Keys.TAB).perform()
#for _ in range(120):
#    webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
#sleep(10)
#html = driver.page_source
#sleep(10)
##### Data from a saved copy for testing
with open(file) as zillow:
    html = zillow.read()

soup = BeautifulSoup(html, "html.parser")
#print(soup)

prop_prices = soup.select('div[class*="StyledPropertyCardDataArea"]')
prices = [price.text.split("+")[0] for price in prop_prices if "$" in price.text.split("+")[0]]
#print(len(prices))

prop_links = soup.select('a[data-test="property-card-link"]')
links = [link['href'] for link in prop_links]
links = list(dict.fromkeys(links))
#print(len(links))

prop_addresses = soup.select('address[data-test="property-card-addr"]')
addresses = [address.text for address in prop_addresses]
#print(len(addresses))

## Zillow does some screwy dynamic loading so we'll just take as many as loaded completely.
number_list = min(len(prices), len(links), len(addresses))

driver.get(form_url)
sleep(2)
for each in range(number_list):
    address = addresses[each]
    price = prices[each]
    link = links[each]
    if "zillow" not in link:
        link = "http://www.zillow.com"+link
    form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form.click()
    form.send_keys(address)
    form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form.send_keys(price)
    form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form.send_keys(link)
    form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    form.click()
    sleep(2)
    form = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    form.click()
    sleep(2)

## Load Google Form
## loop through BS Data into form
## Verify on Google Docs




#driver.quit()