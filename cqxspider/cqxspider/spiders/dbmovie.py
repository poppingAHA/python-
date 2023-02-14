import scrapy
from cqxspider.items import CqxspiderItem


class DbmovieSpider(scrapy.Spider):
    name = 'dbmovie'
    allowed_domains = ['movie.douban.com/']
    start_urls = ['http://movie.douban.com/']

    def parse(self, response):
        # print(response.text)
        result = response.xpath('/html/body/div[3]/div[1]/div/div[2]/div[2]/div[2]/ul/li')

        # print(result)

        for a in result:
            item = CqxspiderItem()
            item['title'] = a.xpath('./@data-title').get()
            item['release'] = a.xpath('./@data-release').get()
            item['rate'] = a.xpath('./@data-rate').get()
            item['star'] = a.xpath('./@data-star').get()
            item['ticket'] = a.xpath('./@data-ticket').get()
            item['duration'] = a.xpath('./@data-duration').get()
            item['region'] = a.xpath('./@data-region').get()
            item['director'] = a.xpath('./@data-director').get()
            item['actors'] = a.xpath('./@data-actors').get()

            yield item
