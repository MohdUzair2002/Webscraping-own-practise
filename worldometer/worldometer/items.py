# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from traceback import print_exception
import scrapy



class WorldometerItem(scrapy.Item):
    # Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html




    Title = scrapy.Field()
    Price = scrapy.Field()
    Description = scrapy.Field()
    ProductID = scrapy.Field()
    Sellername = scrapy.Field()
    SellerID = scrapy.Field()
    URL = scrapy.Field()
    Image=scrapy.Field()


    pass
