## The original purpose of this lesson was to find and auto apply to jobs on Linked in.
## Because of 2-factor, and I don't want to bother setting up a fake account I've changed the purpose
## Instead it will search jobs, and output 20 of them to a file in a list.
## This also will still allow pushing through the process some to use the "filters" section, ie no notes. complex apply

from selenium import webdriver
from selenium.webdriver.common.by import By
from auth import *
import mailer_class

jobs_to_search = ["Python Developer", "Java Developer"]
#jobs_to_search = ["Python Developer"]

message = ""
mailer=mailer_class.Mailer()

url = "https://www.linkedin.com/jobs/"

for job in jobs_to_search:
    if job not in message:
        message += f"Job Postings for: {job}\n\n"


    url = f"https://www.linkedin.com/jobs/search/?currentJobId=3306349089&f_LF=f_AL&geoId=102257491&keywords={job}&location=London%2C%20England%2C%20United%20Kingdom"

    chrome_driver_path = local_driver
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(url)

    job_links = driver.find_elements(By.CLASS_NAME, value="hidden-nested-link")
    for each in range(0,10):
        message += f"{job_links[each].text}\n{job_links[each].get_attribute('href')}\n\n"

    driver.quit()

message = f"Subject: Recent Linked In Job Postings\n\n{message} - Mailer Bot"
#print(message)
mailer.send_email(message)

