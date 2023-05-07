import scrapy


class SkateDSpider(scrapy.Spider):
    name = "skate-d"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
