import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = "phillip.dev.ops@gmail.com"
password = "pmvo zpmq csqe ihlq"

AMAZON_ITEM_URL="https://www.amazon.com/dp/B09XVH9ZWQ/?coliid=I1G7EW62EM5RCR&colid=2YQA025IM8F4H&ref_=list_c_wl_lv_ov_lig_dp_it&th=1"

header = {
    "User-Agent": "Defined",
    "Accept-Language": "en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6"
}

def alert_user(productTitle,itemPrice):
    message = f"{productTitle} is now ${itemPrice}\n{AMAZON_ITEM_URL}"
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pac_man7474@yahoo.com", #to_addrs="tchris9499@gmail.com",
            msg=f"Subject:Item on Sale\n\n{message}"
        )

response = requests.get(AMAZON_ITEM_URL,headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text,"lxml")
#print(soup)
price_section = soup.find(name="span",class_="a-offscreen")
product_title_section = soup.find(name="span",id="productTitle")
productTitle = product_title_section.getText().strip()

itemPrice = float(price_section.getText().split("$")[1])
pricePoint = 175.00
if itemPrice < pricePoint:
    alert_user(productTitle,itemPrice)

