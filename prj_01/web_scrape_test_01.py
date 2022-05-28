import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.co.uk/Shanker-Golf-Balls-Horrible-Golfers/dp/B07WTCLQX3/ref=sr_1_5?keywords=golf&qid=1640552996&sr=8-5"

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

page = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(page.content, "lxml")
#print(soup)
#quit()
##############################################################
# product title
title = soup.find(id='productTitle').get_text().strip()
print("1. Title = " + title)
quit()

# to prevent script from crashing when there isn't a price for the product
try:
    price = float(soup.find(id='priceblock_ourprice').get_text().replace('.', '').replace('€', '').replace(',', '.').strip())
except:
    price = ''

# review score
review_score = float(soup.select('.a-star-4-5')[0].get_text().split(' ')[0].replace(",", "."))

# how many reviews
review_count = int(soup.select('#acrCustomerReviewText')[0].get_text().split(' ')[0].replace(".", ""))

# checking if there is "Out of stock" and if not, it means the product is available
try:
    soup.select('#availability .a-color-state')[0].get_text().strip()
    stock = 'Out of Stock'
except:
    stock = 'Available'