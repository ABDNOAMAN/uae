import scrapy


class ShoesDSpider(scrapy.Spider):
    name = "shoes-d"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
