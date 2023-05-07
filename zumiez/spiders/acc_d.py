import scrapy


class AccDSpider(scrapy.Spider):
    name = "acc-d"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
