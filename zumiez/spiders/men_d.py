import scrapy


class MenDSpider(scrapy.Spider):
    name = "men-d"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
