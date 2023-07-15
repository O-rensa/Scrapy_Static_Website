# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DelawareProjectItem(Item):
    name = Field()
    date_time = Field()
    address  = Field()
    website = Field()
    url = Field()