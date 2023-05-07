import scrapy


class ShoesLSpider(scrapy.Spider):
    name = "shoes-l"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass
