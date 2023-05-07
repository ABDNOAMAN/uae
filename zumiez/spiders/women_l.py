import scrapy


class WomenLSpider(scrapy.Spider):
    name = "women-l"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
