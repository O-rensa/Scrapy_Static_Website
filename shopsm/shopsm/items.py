# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class ShopsmItem(Item):
    # define the fields for your item here like:
    name = Field()
    brand = Field()
    srp = Field()
    disc_price = Field()
    url = Field()
