from os.path import dirname
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import random
import time
import re
import string
import secrets
import os
import json
import easygui

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

mail_address = easygui.enterbox("Enter your email: ")
driver = webdriver.Chrome(
    ChromeDriverManager().install()
)  # USES CHROMEDRIVERMANAGER TO AUTO UPDATE CHROMEDRIVER

# GENERATE PASSWORD
alphabet = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabet) for i in range(16))
# PASSWORD GENERATION FINISHED

# NAME GENERATION
driver.get("https://en.wikipedia.org/wiki/Special:Random")
temp = driver.find_element_by_class_name("firstHeading").text
for char in string.punctuation:
    temp = temp.replace(char, "")  # REMOVES ALL PUNCTUATION
for char in string.digits:
    temp = temp.replace(char, "")  # REMOVES SPACES
temp = "".join(
    filter(lambda char: char in string.printable, temp)
)  # REMOVES NON ASCII CHARACTERS
name = "".join(temp.split())
name = name[: random.randint(5, 7)]  # KEEPS 5 TO 7 LETTERS OF THE ORIGINAL STRING


randomNumber = random.randint(10000, 99999)


finalName = name + str(randomNumber)
# NAME GENERATION FINISHED

# REDDIT ACCOUNT CREATION
driver.get("https://www.reddit.com/register/")

driver.find_element_by_id("regEmail").send_keys(mail_address)
driver.find_element_by_xpath('//button[@data-step="email"]').click()
time.sleep(1)
driver.find_element_by_id("regUsername").send_keys(finalName)
driver.find_element_by_id("regPassword").send_keys(password)
WebDriverWait(driver, 650).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//button[@data-step=\"<Macro 'step'>\"]")
    )
)

driver.get("https://www.reddit.com/prefs/apps")
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(),'create an app...')]").click()
time.sleep(1)
driver.find_element_by_xpath(
    '//*[@id="create-app"]/table/tbody/tr[1]/td/input'
).send_keys("My app")
driver.find_element_by_id("app_type_script").click()
driver.find_element_by_xpath(
    '//*[@id="create-app"]/table/tbody/tr[7]/td/input'
).send_keys("http://www.google.com")
driver.find_element_by_xpath('//*[@id="create-app"]/button').click()
time.sleep(1)
client_id = driver.find_element(
    by=By.XPATH, value='//*[@id="developed-apps"]/ul/li//h3[2]'
).text
client_secret = driver.find_element(
    by=By.XPATH, value='//*[@id="developed-apps"]/ul/li//tbody/tr/td'
).text

config_file = "../config.json"
# read json from config file
with open(config_file) as json_file:
    data = json.load(json_file)

data["workers"][finalName] = {
    "password": password,
    "client_id": client_id,
    "client_secret": client_secret,
    "start_coords": [0, 0],
}

# write json to config file
with open(config_file, "w") as json_file:
    json.dump(data, json_file, sort_keys=True, indent=4)


# driver.close()1
