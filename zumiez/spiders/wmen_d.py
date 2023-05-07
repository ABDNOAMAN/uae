import scrapy


class WmenDSpider(scrapy.Spider):
    name = "wmen-d"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
