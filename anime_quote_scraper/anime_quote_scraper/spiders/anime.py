import scrapy
from anime_quote_scraper.items import AnimeQuoteScraperItem
from scrapy.loader import ItemLoader

class AnimeSpider(scrapy.Spider):
    name = "anime"

    def start_requests(self):
        for url in range(1,10):
            link = f'https://www.goodreads.com/quotes/tag/anime?page={url}'
            yield scrapy.Request(link, self.parse)
    
    def parse(self, response):
        containers = response.css('div.quote.mediumText')
        for i in containers:
            quote = 'div.quoteText'
            author = 'div.quoteText span.authorOrTitle::text'
            title = 'a.authorOrTitle::text'
            
            loader = ItemLoader(item=AnimeQuoteScraperItem(), selector = i)
            
            loader.add_css('quote', quote)
            loader.add_css('author', author)
            loader.add_css('title', title)
            
            yield loader.load_item()

            pass



