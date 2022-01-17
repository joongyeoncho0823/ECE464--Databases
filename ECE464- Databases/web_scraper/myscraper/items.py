# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    genre = scrapy.Field()
    # inStock = scrapy.Field()

    #title 
    #link
    #genre
    #price
    #in stock