import re

import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os

LISTING_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeDvNY_dO9w2_ztk-X5PPnLGhW5i0cRbKJwIjSRArvn_etDfw/viewform?usp=dialog"
ZILLOW_PAGE = "https://appbrewery.github.io/Zillow-Clone/"



header = {'user-agent': "my-app/0.0.1"}

response = requests.get(ZILLOW_PAGE,headers=header)
soup = BeautifulSoup(response.text,"lxml")
card_links = soup.find_all("a",class_="property-card-link")
links = []
for href in card_links:
    links.append(href.get("href"))
property_card_price_list = soup.find_all(attrs={"data-test": "property-card-price"})
price_list = []
for price in property_card_price_list:
    listed = price.getText()
    listed = re.split('[+ /]',listed)[0]
    price_list.append(listed)
property_addr_cards = soup.find_all(attrs={"data-test": "property-card-addr"})
address_list = []
for address in property_addr_cards:
    address_list.append(address.getText())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(),"chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(LISTING_FORM_URL)
wait = WebDriverWait(driver, 2)



for listing in range(len(address_list)):
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    inputs = driver.find_elements(By.XPATH, "//input[@type='text']")
    inputs[0].send_keys(address_list[listing])
    inputs[1].send_keys(price_list[listing])
    inputs[2].send_keys(links[listing])
    submit_button = driver.find_element(By.XPATH,"//div[@role='button']")
    submit_button.click()
    wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/a")))
    submit_another = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    submit_another.click()
