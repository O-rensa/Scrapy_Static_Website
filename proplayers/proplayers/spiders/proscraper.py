import scrapy
from proplayers.items import ProplayersItem
from scrapy.loader import ItemLoader

class ProscraperSpider(scrapy.Spider):
    name = "proscraper"
    allowed_domains = ["https://dota2.fandom.com/wiki/Professional_players"]
    start_urls = ["https://dota2.fandom.com/wiki/Professional_players"]

    def parse(self, response):

        for data in response.css('table.cargoDynamicTable.display').css('tbody tr'):
            loader = ItemLoader(item = ProplayersItem())

            loader.add_value('player_id', data.css('td a::attr(title)').get())
            loader.add_value('name', data.css('td::text')[1].get())
            loader.add_value('country', data.css('td::text')[2].get())
            loader.add_value('article', data.css('td a::attr(href)').get())

            yield loader.load_item()