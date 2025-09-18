from selenium import webdriver
from selenium.webdriver.common.by import  By
import datetime as dt

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

def click_add_on():
    add_ons = driver.find_elements(By.CLASS_NAME,value="product.unlocked.enabled")
    num_add_ons = len(add_ons)

    if num_add_ons > 0:
        add_ons[num_add_ons-1].click()

def check_seconds():
    global current_seconds
    global next_seconds_check
    current_seconds = int(dt.datetime.now().second)
    if current_seconds >= next_seconds_check:
        click_add_on()
        next_seconds_check = current_seconds + 5
        if next_seconds_check > 60:
            next_seconds_check -= 60


start_time = int(dt.datetime.now().minute)
current_time = start_time
end_time = start_time + 5

cookie = driver.find_element(By.CSS_SELECTOR,"#bigCookie")

current_seconds = int(dt.datetime.now().second)
next_seconds_check = current_seconds + 1
if next_seconds_check > 60:
    next_seconds_check -= 60
while current_time<=end_time:
    cookie.click()
    current_time = int(dt.datetime.now().minute)
    check_seconds()
