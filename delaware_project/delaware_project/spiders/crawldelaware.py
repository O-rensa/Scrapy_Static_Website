from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.items import DelawareProjectItem


class CrawldelawareSpider(CrawlSpider):
    name = "crawldelaware"
    allowed_domains = ["visitdelaware.com"]
    urls  = []
    for i in range (0,144):
        urls_format = f"https://www.visitdelaware.com/events?page={i}"
        urls.append(urls_format)
    start_urls = urls

    rules = (
        Rule(LinkExtractor(allow = r'(/events/)[a-z\-0-9]*(/)[0-9]*(/)[0-9]*'), follow = False, callback = 'parse_items')
        ,)

    def parse_items(self, response):
        name = response.css('div.main-left-column h1::text').get()
        date_time = response.css('div.field--type-datetime time::text').get()
        address = response.css('div.address p::text').get().strip().replace('\n', '')
        website = response.css('a.website-link::attr("href")').get()
        url = response.url

        items = DelawareProjectItem()
        items['name'] = name
        items['date_time'] = date_time
        items['address'] = address
        items['website'] = website
        items['url'] = url

        yield  items
        
        

