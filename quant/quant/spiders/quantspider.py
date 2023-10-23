import scrapy
# from scrapy_playwright.page import PageCoroutine
from scrapy_splash import SplashRequest




# scrapy.http.Response()
class Spider(scrapy.Spider):
    name='quant'
    start_urls = ["https://announcements.bybit.com/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, meta={'playwright': True})
            # yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        for link in response.css('.article-list>a::attr(href)'):
            yield response.follow(link, callback=self.parse_new)
        for i in range(2,10):
            next_page = f'https://announcements.bybit.com/en-US/?category=&page={i}'
            yield response.follow(next_page, callback = self.parse)

    def parse_new(self, response):    
        yield {
            "name":response.css('.article-detail-title::text').get(),
            "body":response.css('.article-detail-content p::text').get()
        }

    
