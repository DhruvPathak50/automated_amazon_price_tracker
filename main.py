from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.amazon.com/SAMSUNG-27-inch-Border-Less-FreeSync-LF27T350FHNXZA/dp/B08FF3JQ28/ref=sr_1_3?crid=2ALUPMEVELDQJ&dib=eyJ2IjoiMSJ9.H5GDIy5seBP0_Yw4-i4uuX9Qt4rQ_s1_KxYMGrzzvlTMvcB0HUsZeqO5bhawQtZmItcayX8vOnhstPFNcMgsJ1snmJUbROa0NPQ1Ai8g4Mc1W7142Ju3xPgW2JgHsXWCrt76oe5C7gsHnfkmDY26BNnEPFZQAHPOWbEBlq-7piTGJIh6X1iCitkrmYiHwmfsWWrkHXcdHF6_3R4kEBasskxAOiMQcaQHjfFzNbzCYZk.3XOb4BQIVwDBfbdFuBzxYWSm0nkYmSacZpOhJts1nxs&dib_tag=se&keywords=monitor%2Bsamsung&qid=1724405641&sprefix=monitor%2Bsam%2Caps%2C431&sr=8-3&th=1")
data = response.text
# print(data)

bs = BeautifulSoup(data, 'html.parser')
# print(bs.prettify())
tag = bs.find(name="span", class_="a-offscreen")
price = tag.getText()
print(price)
