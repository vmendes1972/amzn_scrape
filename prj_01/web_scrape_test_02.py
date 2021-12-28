from bs4 import BeautifulSoup
import requests

#File = open("out.csv", "a")
url = "https://www.amazon.co.uk/dp/B09BC711XN/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B09BC711XN&pd_rd_w=sPfGn&pf_rd_p=828203ef-618e-4303-a028-460d6b615038&pd_rd_wg=hF2Gh&pf_rd_r=6SKEBB7WM5ZRY0DXPAZ6&pd_rd_r=4118f6fc-2201-4902-a3de-dc45a023beb3&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE3OFNURFEzUTA4NDUmZW5jcnlwdGVkSWQ9QTA2NDg2MzFFRlVWUVQxOEQwSVAmZW5jcnlwdGVkQWRJZD1BMDgwNTE3NDJPUFlWVUlKUk1XUDkmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
						'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(webpage.content, features="lxml")

print(soup)

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
