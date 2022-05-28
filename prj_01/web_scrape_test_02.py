from bs4 import BeautifulSoup
import requests

#File = open("out.csv", "a")
url = "https://www.amazon.co.uk/Grano-Milano-Nespresso-Compatible-Flavoured/dp/B081RPS7Z5/ref=sr_1_2_sspa?keywords=decaf%2Bpods%2Bnespresso%2Bcompatible&qid=1640720887&s=grocery&sprefix=decaf%2Bpods%2Cgrocery%2C61&sr=1-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzSTBSVzREMlE1WkxWJmVuY3J5cHRlZElkPUEwMTI3OTUwS0Q4V0FUWVNZOFdFJmVuY3J5cHRlZEFkSWQ9QTA0NDI1NzAxVjk0WU9HQUFNSkJQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
						'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(webpage.content, features="html.parser")

#print(soup)

##############
#retrieve title
try:
    title = soup.find("span", attrs={"id": 'productTitle'})
    title_value = title.string
    title_string = title_value.strip().replace(',', '')    		
except AttributeError:
	title_string = "NA"
print("product Title = ", title_string)

##########################
# retrieving price
try:
    price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
        # we are omitting unnecessary spaces
        # and commas form our string
except AttributeError:
    price = "NA"
print("Products price = ", price)

###########################
# retrieving product rating
try:
    rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')
except AttributeError:
    try:
        rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
    except:
        rating = "NA"
print("Overall rating = ", rating)

###########################
# retrieving customer reviews
try:
    review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')
except AttributeError:
    review_count = "NA"
print("Total reviews = ", review_count)
 
#############################
# print availablility status
try:
    available = soup.find("div", attrs={'id': 'availability'})
    available = available.find("span").string.strip().replace(',', '')
except AttributeError:
    available = "NA"
print("Availability = ", available)

###################
# print sold by
try:
    soldby = soup.find("span", attrs={'id': 'sellerProfileTriggerId'}).string.strip().replace(',', '')
except AttributeError:
    soldby = "NA"
print("Sold By = ", soldby)
