import scrapy
from bs4 import BeautifulSoup
import re
from ..items import BlueTomatoScrapperItem


class EcomspiderSpider(scrapy.Spider):
    name = 'ecomspider'
    allowed_domains = ['www.blue-tomato.com']
    start_urls = ['https://www.blue-tomato.com/de-AT/products/categories/Snowboard+Shop-00000000/?page='
                  + str(i+1) for i in range(34)]

    def parse(self, response):
        item = BlueTomatoScrapperItem()
        
        Title = response.css('.track-load-producttile::attr(data-productname)').extract()
        Brand = response.css('.track-load-producttile::attr(data-brand)').extract()
        Price = response.css('span.price::text').extract()
        Image_Url = response.css('span.productimage img::attr(src)').extract()
        Product_Url = response.css('.track-load-producttile::attr(href)').extract()
        
        item['Name']           = Title
        item['Brand']          = Brand
        item['Price']          = Price
        item['Image_Url']       = Image_Url
        item['Product_Url']     = Product_Url
        return item
        
        pass
