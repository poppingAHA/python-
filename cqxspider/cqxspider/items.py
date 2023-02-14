# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CqxspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 电影名称
    release = scrapy.Field()  # 年份
    rate = scrapy.Field()  # 评分
    star = scrapy.Field()  # 星级
    ticket = scrapy.Field()  # 网址
    duration = scrapy.Field()  # 电影时长
    region = scrapy.Field()  # 电影产地
    director = scrapy.Field()  # 导演
    actors = scrapy.Field()  # 演员
