import os
import smtplib
from dotenv import load_dotenv


import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/SAMSUNG-27-inch-Border-Less-FreeSync-LF27T350FHNXZA/dp/B08FF3JQ28/ref=sr_1_5?crid=B3NOBWECR116&dib=eyJ2IjoiMSJ9.HkCfZ_3N4KnLA4nkOFIBY06feBVS_BBME5iwKwRw70fEmKfR8IDjXlnumnAkTqIlF6w27iOfuPeQXWWjk3nEEIW3xEapCQykyHGWnC9nXJX4F6CdpQP9K8y16YANp7rrkJpmf50oKp30GPhBLMgRjivLNL2lYsQuLi-FuaI_JxDawpQEhvNmYB7lNpPjPTJ77bztlwb4uzBXgMChz-LG89ZVv5Msq095AutMkfwYVBI.ioyzsksnHbpCXB6n_xFDq83lOa_ohGv05bH3CcwhXKw&dib_tag=se&keywords=samsung%2Bmonitor&qid=1724410170&sprefix=sams%2Caps%2C501&sr=8-5&th=1"
load_dotenv()
header ={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-IN,en;q=0.9,mr-IN;q=0.8,mr;q=0.7,en-GB;q=0.6,en-US;q=0.5,hi;q=0.4",
"Priority": "u=0, i",
# "Sec-Ch-Ua": ""Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"",
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": "Windows",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}
response = requests.get(url, headers=header)
data = response.text
# print(data)

bs = BeautifulSoup(data, 'html.parser')
# print(bs.prettify())
tag = bs.find(name="span", class_="a-offscreen")
# tag = bs.select_one(selector="span span .a-price-whole")
# print(tag)

current_price = float(tag.getText()[1:])

print(current_price)
target_price = 87.00
# if current_price <= target_price:
#     # email me
#     smtp = os.getenv('SMTP_ADDRESS')
#     email = os.getenv('EMAIL_ADDRESS')
#     password = os.getenv('EMAIL_PASSWORD')
    # with smtplib.SMTP(host=smtp) as s:
    #     s.starttls()
    #     s.login(user=email, password=password)
    #     s.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: Buy this "
    #                                                                                             f"monitor Now!\n\nPrice "
    #                                                                                             f"of this samsung monitor "
    #                                                                                             f"has fallen off to "
    #                                                                                             f"{current_price} which "
    #                                                                                             f"is below your set "
    #                                                                                             f"target price."
    #                f"URL = {url}")
