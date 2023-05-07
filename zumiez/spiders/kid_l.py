import scrapy


class KidLSpider(scrapy.Spider):
    name = "kid-l"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
