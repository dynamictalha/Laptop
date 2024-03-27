import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html")

# ----------------Product Name------------

products = soup.find_all("a", class_ = "title")
# print(products)
product_list = []
for i in products:
    name = i.text
    # print(name)
    product_list.append(name)
# print(product_list)

# ----------------Price------------
prices = soup.find_all("h4",class_ = "float-end price card-title pull-right")
# print(prices)
prices_list = []
for i in prices:
    price = i.text
    # print(price)
    prices_list.append(price)

# print(prices_list)

# ----------------detail------------
details = soup.find_all("p", class_ = "description card-text")
detail_list = []
for i in details:
    detail = i.text
    detail_list.append(detail)

# print(detail_list)
    

# ----------------Reviews------------
reviews = soup.find_all("p",class_ = "float-end review-count")
review_list = []
for i in reviews:
    review = i.text
    review_list.append(review)

# print(review_list)
    
df = pd.DataFrame({"Products Name":product_list,"Details": detail_list,"Prices":prices_list,"Reviews": review_list })
# print(df)

df.to_csv("Laptops.csv")



