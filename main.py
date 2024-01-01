from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os

my_id = os.environ['mail_id']
my_password = os.environ['mail_id_pass']

header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get("https://www.amazon.in/Refurbished-Samsung-33-78cm-Fingerprint-NP930XED-KB2IN/dp/B0BXP1GTPT/ref=sr_1_6?crid=1PRW3GUJLBWM3&keywords=book2+pro&qid=1702470210&sprefix=book2%2Caps%2C222&sr=8-6", headers=header)

soup = BeautifulSoup(response.content, "lxml" )

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
price_seperated  = price_without_currency.split(",")
price_in_string =""
for str in price_seperated:
    price_in_string = price_in_string+str
price_as_float = float(price_in_string)
print(price_as_float)

if price_as_float <= 95000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_id, my_password)
        connection.sendmail(
            from_addr=my_id,
            to_addrs=my_id,
            msg=f"Subject: Time to buy samsung book 2 pro\n\nThe product you want to buy in amazon has reduced to {price_as_float}.this is the time to buy the product."
        )
