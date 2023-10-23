import scrapy, json
# from scrapy_playwright.page import PageCoroutine

from bs4 import BeautifulSoup



# scrapy.http.Response()
class Spider(scrapy.Spider):
    name='quant'
    start_urls = ["https://announcements.bybit.com/"]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, meta={'playwright': True})
    #         # yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        for link in response.css('.article-list>a::attr(href)'):
            yield response.follow(link, callback=self.parse_new)
        for i in range(2,10):
            next_page = f'https://announcements.bybit.com/en-US/?category=&page={i}'
            yield response.follow(next_page, callback = self.parse)

    def parse_new(self, response):   
        html = BeautifulSoup(response.text)
        json_ = json.loads(html.body.find('script', attrs={'id':'__NEXT_DATA__'}).text)
        
        yield {
            "name": json_['props']['pageProps']['articleDetail']['title'],
            "body": '\n'.join([
                ' '.join([inner_c.get('text', '') for inner_c in c['children']
                 ]) for c in json_['props']['pageProps']['articleDetail']['content']['json']['children']])
        }

    
