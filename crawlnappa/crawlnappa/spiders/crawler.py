from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from crawlnappa.items import CrawlnappaItem

class CrawlingSpider(CrawlSpider):
    name = 'crawlnappa'
    allowed_domains = ['nappadori.com']
    start_urls = ['https://global.nappadori.com/']

    rules = (
        Rule(LinkExtractor(allow='collections')),
        Rule(LinkExtractor(allow='products'), callback= 'parse_data')
        ,)
    
    def parse_data(self, response):
        var_name = response.css('div.ProductMeta h1.ProductMeta__Title::text').get()
        var_dup_color_price = response.css('div.ProductForm__Variants select[title = "Variant"] option::text').getall()

        var_color_price = []

        for i in var_dup_color_price:
            if i not in var_color_price:
                var_color_price.append(i)

        nappadori_products = CrawlnappaItem()

        nappadori_products['name'] = var_name
        nappadori_products['color_price'] = var_color_price

        yield nappadori_products