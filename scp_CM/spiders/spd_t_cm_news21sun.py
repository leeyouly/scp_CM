# -*- coding: UTF-8 -*-
import scrapy
from scp_CM.items import CM_WebSiteItem
import re
import lxml
from lxml import etree
import time, datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

today = datetime.datetime.now()
day_datadate = today.strftime('%Y-%m-%d')
year_datadate = today.strftime('%Y')
last_year = int(year_datadate) - 1
last_update_date = datetime.datetime.now() - datetime.timedelta(days=10)

index = 1

#军工需求，抓取中国工程机械商贸网新闻
class PuokNEA(scrapy.Spider):
    name = "spd_t_cm_news21sun"
    start_urls = (
        'http://news.21-sun.com',
    )
    ignore_page_incremental = True

    def parse(self,response):
        self.crawler.stats.set_value('spiderlog/source_name', u'中国工程机械商贸网')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_CM_WEBSITE_NEWS'])

        # pageUrl = 'http://news.21-sun.com/pro/pro_2_1.htm'
        #采集历史，循环读取
        for page in range(1,10,1):
            # pageUrl = 'http://news.21-sun.com/pro/pro_2_' + str(1) + '.htm'
            pageUrl = 'http://news.21-sun.com/tools/getProlist.jsp?nowPages=' + str(page) +'&_=1524813923367'
            request = scrapy.http.FormRequest(pageUrl, callback=self.parse_title)
            request.meta['website_name'] = u'中国工程机械商贸网'
            yield request


    #解析文章标题以及url
    def parse_title(self, response):
        # newsUl = response.xpath('//*[@id="prolist"]/ul')
        # html_parser = lxml.html.HTMLParser(encoding='gb2312', remove_comments=True)
        # content_html_etree = lxml.html.fromstring(response.body, parser=html_parser)
        # lxml.etree.strip_elements(content_html_etree, 'iframe', 'script', 'style')
        # news_html = lxml.html.tostring(content_html_etree, encoding='utf-8').decode('utf-8')

        html = etree.HTML(response.body).xpath('//li')
        for news in html:
            # news = newsList.xpath('./li')
            if news.xpath('//a/@href') <> []:
                for newsHref in news.xpath('//a/@href'):
                    if 'list' in newsHref:
                        continue
                    newsHref = response.urljoin(newsHref)
                    # print newsHref

                    request = scrapy.http.Request(newsHref, callback=self.parse_newsContent)
                    request.meta['website_name'] = response.meta['website_name']
                    yield request
            else:
                print u'未找到url'

    #解析文章内容
    def parse_newsContent(self, response):
        # datadate = datetime.datetime.strptime(response.meta['datadate'], '%Y-%m-%d')
        newsTitle = response.xpath('.//div[@class="contTitle"]/h3').extract()[0]
        datadateStr = response.xpath('.//div[@class="tipLeft l"]/span[@class="time l"]/text()').extract()[0].strip()
        print datadateStr
        datadate = datetime.datetime.strptime(datadateStr, '%Y-%m-%d')

        contentHtml = response.xpath('//*[@id="content"]')
        contentString = ''
        for content in contentHtml:
            if content.xpath('.//text()').extract()<>[] :

                for contentStr in content.xpath('.//text()').extract():
                    contentString = contentString + contentStr
                    # contentString = contentString + '\n'

        item = CM_WebSiteItem()
        item['datadate'] = datadate
        item['news_title'] =newsTitle
        item['news_type'] = u'产品动态'
        item['website_name'] = response.meta['website_name']
        item['news_html'] = u''
        item['news_contenturl'] = response.url
        item['news_imageurl'] = u''
        item['update_dt'] = datetime.datetime.now()
        item['news_content'] = contentString
        yield item
