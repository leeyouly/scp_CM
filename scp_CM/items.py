# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScpCmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CM_publicItem(scrapy.Item):
    datadate = scrapy.Field()
    public_name = scrapy.Field()
    public_Id = scrapy.Field()
    news_title = scrapy.Field()
    news_content = scrapy.Field()
    news_html = scrapy.Field()
    news_contenturl = scrapy.Field()
    news_imageurl = scrapy.Field()
    update_dt = scrapy.Field()


class CM_WebSiteItem(scrapy.Item):
    datadate = scrapy.Field()
    news_type = scrapy.Field()
    news_title = scrapy.Field()
    website_name = scrapy.Field()
    news_content = scrapy.Field()
    news_html = scrapy.Field()
    news_contenturl = scrapy.Field()
    news_imageurl = scrapy.Field()
    update_dt = scrapy.Field()
    source = scrapy.Field()