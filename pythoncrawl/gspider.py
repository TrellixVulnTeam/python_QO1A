import scrapy


class GspiderSpider(scrapy.Spider):
    name = 'gspider'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        pass
