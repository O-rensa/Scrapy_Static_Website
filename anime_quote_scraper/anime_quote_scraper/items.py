# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def cleaner(string):
    string = string.split('\n')
    return string[1].strip().replace('<br>', ' ').replace('\"',' ')

class AnimeQuoteScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    quote = scrapy.Field(
        input_processor = MapCompose(cleaner),
        output_processor = TakeFirst()
    )
    author = scrapy.Field(
        input_processor = MapCompose(cleaner),
        output_processor = TakeFirst()
    )
    title = scrapy.Field(
        output_processor = TakeFirst()
    )
