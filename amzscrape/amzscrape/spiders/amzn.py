import scrapy

class AmznSpider(scrapy.Spider):
    name = 'amzn'
    #allowed_domains = ['amazon.co.uk']
    start_urls = ['https://www.amazon.co.uk/s?k=headphones']
    
    def parse(self, response):
        name:response.css('.a-size-medium a-color-base a-text-normal')

