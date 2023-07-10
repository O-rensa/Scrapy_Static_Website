from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from shopsm.items import ShopsmItem

class CrawlshopsmSpider(CrawlSpider):
    name = "crawlshopsm"
    allowed_domains = ["shopsm.com"]
    total_pages = 422
    links  = []
    for page in range(1,total_pages+1):
        page_num = str(page)
        links.append(f"https://www.shopsm.com/collections/sale-items?page={page_num}")
    
    start_urls = links

    rules = (
            Rule(LinkExtractor(allow = r"(collections/sale-items/products/)[a-z0-9\s\'\-]*([^(wo)](men))[a-z0-9\s\'\-]*"),
                 callback='parse_item', follow=False
                 ),
            Rule(LinkExtractor(
                restrict_css = 'div div a.text-14',
                 restrict_text= r"[a-zA-Z0-9\s\'\-]*([^(W|w)(O|o)](M|m)(E|e)(N|n))[a-zA-Z0-9\s\'\-]*"
                               ), callback='parse_item', follow=False)
            ,)

    def parse_item(self, response):
        var_data = ShopsmItem()
        var_data['name'] = response.css('div div div h1.text-xl::text').get()
        var_data['brand'] = response.css('div a p.text-sm::text').get()
        var_data['srp'] = response.css('p.text-sm.line-through::text').get()
        var_data['disc_price'] = response.css('p.text-xl.font-medium.text-saleRed-500::text').get()
        var_data['url'] = response.url
        
        yield var_data
        
