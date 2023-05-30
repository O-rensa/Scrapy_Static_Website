import scrapy

#hello

class PlayerscraperSpider(scrapy.Spider):
    name = "playerscraper"
    allowed_domains = ['https://dota2.fandom.com/wiki/Professional_players']
    start_urls = ['https://dota2.fandom.com/wiki/Professional_players']

    def parse(self, response):
        player = response.css('table.wikitable.sortable').css('tbody tr')
        for i in range(1,len(player.get()) + 1):
            yield {
            'player_id' : player[i].css('span.new::text').get(),
            'name': player[i].css('td::text')[0].get(),
            'country': player[i].css('td::text')[1].get()
            }
            