from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth import *
from time import sleep
import tweepy

class TwitterBot():

    def __init__(self):
        self.speed_url = "https://www.speedof.me"
        self.twitter_url = "https://twitter.com/i/flow/login"
        self.driver = webdriver.Chrome(executable_path=local_driver)
        self.dl_speed = 0
        self.ul_speed = 0
        self.message = ""

    def test_speed(self):
        self.driver.get(self.speed_url)
        sleep(5)
        self.driver.find_element(By.LINK_TEXT, value="ACCEPT").click()
        sleep(5)
        self.driver.find_element(By.ID, value="start_test_btn").click()
        sleep(60)
        speeds = self.driver.find_elements(By.CLASS_NAME, value = "progress-realtime-speed")
        ## Returns a list: Download Average, Upload Average, Latency, IP Address, Test Server
        self.message = f"Speed Test: {speeds[0].text}Mb Down, {speeds[1].text}Mb Up, {speeds[2].text}ms Ping via speedof.me."
        self.driver.close()


    def send_tweet(self, message):
        #print(message)
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        api.update_status(status=message)


