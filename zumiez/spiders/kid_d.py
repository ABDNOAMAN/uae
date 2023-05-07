import scrapy


class KidDSpider(scrapy.Spider):
    name = "kid-d"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
