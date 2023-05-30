# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def article_process(text):
    return 'https://dota2.fandom.com' + str(text)

class ProplayersItem(scrapy.Item):
    player_id = scrapy.Field(
        output_processor = TakeFirst()
    )
    name = scrapy.Field(
        output_processor = TakeFirst()
    )
    country = scrapy.Field(
        output_processor = TakeFirst()
    )
    article = scrapy.Field(
        input_processor = MapCompose(article_process),
        output_processor = TakeFirst()
    )
