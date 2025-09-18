from selenium import webdriver
from selenium.webdriver.common.by import  By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B09XVH9ZWQ/?coliid=I1G7EW62EM5RCR&colid=2YQA025IM8F4H&ref_=list_c_wl_lv_ov_lig_dp_it&th=1")
#
# price_whole = driver.find_element(By.CLASS_NAME,"a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,"a-price-fraction")


# print(f"${price_whole.text}.{price_cents.text}")


driver.get("https://python.org")
#dates = driver.find_elements(By.XPATH,value='/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[1]/time/span')
dates = driver.find_elements(by=By.CSS_SELECTOR,value=".event-widget time")
names = driver.find_elements(by=By.CSS_SELECTOR,value=".event-widget li a")

events = {}


for n in range(0,len(dates)):
    events[n] = {
        "time": dates[n].text,
        "name": names[n].text
    }


print(events)






driver.close()