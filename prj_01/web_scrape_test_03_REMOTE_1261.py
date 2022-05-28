from requests_html import HTMLSession

def getprice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=0)
    
    try:
        product = {
                'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
                'price': r.html.xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]', first=True).text,
                'soldby': r.html.xpath('//*[@id="tabular-buybox"]/div[1]/div[4]/div/span', first=True).text
        }
    except:
        product = {
                'title': "NA",
                'price': "NA",
                'soldby': "NA"
        }
            
    print(product)
    return product

getprice('https://www.amazon.co.uk/dp/B07B2NSKY2;')
#getprice('https://www.amazon.co.uk/dp/B0846MK6VQ;')
#getprice('https://www.amazon.co.uk/dp/B07M9ZLDZ6;')
#getprice('https://www.amazon.co.uk/dp/B07PMS2SFF;')
#getprice('https://www.amazon.co.uk/dp/B078GVS4C4;')
