# Logs into Instagram and follows the first 10 accounts that follow another selected account (to_follow)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth import *
from time import sleep

url = "http://www.instagram.com"
to_follow = "HasbroPulse"

## Full Path to local Chromedriver.exe file
chrome_driver_path = local_driver

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

sleep(2)
# Enter Username
form = driver.find_element(By.XPATH, value = "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
form.send_keys(ig_user)
#Enter Password
form = driver.find_element(By.XPATH, value = "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
form.send_keys(ig_pass)
#Submit Log In
form = driver.find_element(By.XPATH, value = "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
form.click()
#No notifications
sleep(10)
form = driver.find_element(By.XPATH, value = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
form.click()

driver.get(f"{url}/{to_follow}")
sleep(10)
# Open Followers
form = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]")
form.click()
sleep(5)
#Get Follower Buttons

for each in range(1,10):
    path=f"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{each}]/div[3]/button"
    button = driver.find_element(By.XPATH, value = path)
    if button.text == "Follow":
        button.click()
    sleep(3)








driver.quit()