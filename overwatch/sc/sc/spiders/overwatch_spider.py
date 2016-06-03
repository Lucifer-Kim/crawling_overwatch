import scrapy

class OverwatchSpider(scrapy.Spider):
    name = "overwatch"
    allowed_domains = ["http://kr.battle.net/ko/"]
    start_urls = [
        "http://kr.battle.net/forums/ko/overwatch/5018709/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            for sel in response.body:
                author = sel.xpath('//span[@class="ForumTopic-author"]').extract()
                f.write(str(author[0].encode('utf-8')))