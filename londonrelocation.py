import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from property import Property


class LondonrelocationSpider(scrapy.Spider):
    name = 'londonrelocation'
    allowed_domains = ['londonrelocation.com','https://londonrelocation.com/properties-to-rent/',
                       'londonrelocation.com/our-properties-to-rent/properties/']
    start_urls = ['https://londonrelocation.com/properties-to-rent/']

    def parse(self, response):
        for start_url in self.start_urls:
            yield Request(url=start_url,
                          callback=self.parse_area)

    def parse_area(self, response):
        area_urls = response.xpath('.//div[contains(@class,"area-box-pdh")]//h4/a/@href').extract()
        for area_url in area_urls:
            yield Request(url=area_url,
                          callback=self.parse_area_pages)

    def parse_area_pages(self, response):
        # Write your code here and remove `pass` in the following line
        yield{
            'title': response.css('div.h4-space a::text').get().strip(),
            'price': response.css('div.bottom-ic h5::text').get()

            }

        # an example for adding a property to the json list:
        #property = ItemLoader(item=Property())
       
        #property.add_value('title', response.css('div.h4-space a::text'))

        # property = ItemLoader(item=Property())
         #title=property.add_xpath('title','//div[@class="h4-space"]')
         #property.add_value('title', title)
        # property.add_value('price', '1680') # 420 per week
        # property.add_value('url', 'https://londonrelocation.com/properties-to-rent/properties/property-london/534465-2-bed-frognal-hampstead-nw3/')
        #return property.load_item()
