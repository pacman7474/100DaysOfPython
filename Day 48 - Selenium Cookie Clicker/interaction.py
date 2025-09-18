from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_field = driver.find_element(By.NAME,value="fName")
last_name_field = driver.find_element(By.NAME,value="lName")
email_field = driver.find_element(By.NAME,value="email")
first_name_field.send_keys("Phillip")
last_name_field.send_keys("Christensen")
email_field.send_keys("phillip.dev.ops@gmail.com")

button = driver.find_element(By.CLASS_NAME,value="btn")
button.click()

#
# active_editors_string.click()
# search = driver.find_element(By.NAME,"search")
# all_portals.click()
# search.send_keys("Python",Keys.ENTER)
# driver.close()