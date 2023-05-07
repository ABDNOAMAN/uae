import scrapy


class AccLSpider(scrapy.Spider):
    name = "acc-l"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
