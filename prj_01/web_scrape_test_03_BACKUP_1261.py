from requests_html import HTMLSession
<<<<<<< HEAD
import pandas as pd
import csv

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
"Accept-Encoding": "gzip, deflate", 
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
"Dnt": "1", 
"Host": "httpbin.org", 
"Upgrade-Insecure-Requests": "1", 
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
}

def getprice(url):
    s = HTMLSession()    
    r = s.get(url, headers=headers)
    r.html.render(sleep=1)
    
    print(url)
    print(r.json)
    
    try:
        title = r.html.xpath('//*[@id="productTitle"]', first=True).text
    except:
        title = "NA"
        
    try:
        price = r.html.xpath('//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]', first=True).text
    except:
        price = "NA"
        
    try:
        soldby = r.html.xpath('//*[@id="tabular-buybox"]/div[1]/div[4]/div/span', first=True).text
    except:
        soldby = "NA"
    
    product = {
        'title' : title,
        'price' : price,
        'soldby' : soldby
    }
    
    print(title)
    print(price)
    print(soldby)
    print(product)    
    return product
    
df = [{'title': "NA", 'price': "NA", 'soldby': "NA"}]

with open('C:\\Users\\vm100\\Downloads\\Jungle Scout CSV Export.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0
    for row in reader:
        count = count + 1        
        if(count < 10):
            print(count)
            print(row['ASIN'])
            df_append = getprice("https://www.amazon.co.uk/dp/" + row['ASIN'])
            print(df_append)
            #appended_data = df.DataFrame.append(df_append)

#print(appended_data)
#df = pd.read_excel('C:\\Users\\vm100\\Downloads\\Jungle Scout CSV Export.csv') # can also index sheet by name or fetch all sheets
#mylist = df['ASIN'].tolist()
#print(df)

#getprice('https://www.amazon.co.uk/dp/B07B2NSKY2;')
=======

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
>>>>>>> origin/main
#getprice('https://www.amazon.co.uk/dp/B0846MK6VQ;')
#getprice('https://www.amazon.co.uk/dp/B07M9ZLDZ6;')
#getprice('https://www.amazon.co.uk/dp/B07PMS2SFF;')
#getprice('https://www.amazon.co.uk/dp/B078GVS4C4;')
