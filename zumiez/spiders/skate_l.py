import scrapy


class SkateLSpider(scrapy.Spider):
    name = "skate-l"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
