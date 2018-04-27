# -*- coding: UTF-8 -*-
import scrapy
from scp_CM.items import CM_publicItem
import re
import time, datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

today = datetime.datetime.now()
day_datadate = today.strftime('%Y-%m-%d')
year_datadate = today.strftime('%Y')
last_year = int(year_datadate) - 1
last_update_date = datetime.datetime.now() - datetime.timedelta(days=10)

public_dict = {
    'gcjxzzs': u'工程机械杂志社',
    'c_m_weekly': u'工程机械周刊',
    'cmtodaywx': u'今日工程机械',
    'www21sun': u'中国工程机械商贸网',
    'ccma-weixin': u'中国工程机械工业协会',
}

#工程机械杂志社微信公众号
class PuokSteel(scrapy.Spider):
    name = "spd_t_cm_public"
    start_urls = (
        'http://weixin.sogou.com/',
        # 'http://weixin.sogou.com/weixin?query=工程机械杂志社',
    )
    ignore_page_incremental = True

    def parse(self,response):
        self.crawler.stats.set_value('spiderlog/source_name', u'工程机械相关公众号抓取')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_CM_PUBLIC_NEWS'])

        for key in public_dict.keys():
            public_url = 'http://weixin.sogou.com/weixin?query=' + key
            request = scrapy.http.Request(public_url, callback=self.parse_title)
            request.meta['public_Id'] = key
            # request.meta['public_name'] = public_dict[key]
            yield request


    def parse_title(self, response):
        urlstart = response.xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a/@href').extract()[0]

        request = scrapy.http.Request(urlstart, callback=self.parse_content)
        request.meta['public_Id'] = response.meta['public_Id']
        print urlstart
        yield request

    #处理返回的请求
    def parse_content(self, response):
        contentStr = response.body
        listStr = re.findall('var msgList = (.+);', contentStr)
        if listStr <> []:
            newsList = eval(re.findall('var msgList = (.+);',contentStr)[0])
            for newsTypeList in newsList['list']:

                timeStamp = newsTypeList['comm_msg_info']['datetime']
                timeArray = time.localtime(timeStamp)
                # releaseTime = time.strptime(time.strftime("%Y-%m-%d %H:%M:%S", timeArray), '%Y-%m-%d %H:%M:%S')
                releaseTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

                for news in newsTypeList['app_msg_ext_info']['multi_app_msg_item_list']:
                    # titleUrl = 'https://mp.weixin.qq.com' + title['app_msg_ext_info']['multi_app_msg_item_list']['content_url'].replace('amp;','')
                    # titleUrl = 'https://mp.weixin.qq.com' + news['content_url'].replace('amp;','')
                    titleUrl = response.urljoin(news['content_url'].replace('amp;',''))

                    author = news['author']
                    digest = news['digest']
                    titleName = news['title']
                    #处理图片
                    # imageUrlListStr = ''
                    # for imageUrl in news['app_msg_ext_info']['multi_app_msg_item_list']:
                    #     imageUrlListStr = imageUrlListStr + imageUrl['cover'] + ', '

                    request = scrapy.http.Request(titleUrl, callback=self.parse_news)
                    request.meta['title'] = titleName
                    request.meta['datadate'] = releaseTime
                    request.meta['public_Id'] = response.meta['public_Id']
                    # request.meta['imageUrlListStr'] = imageUrlListStr
                    yield request
        else:
            print u'未找到文章列表'


    def parse_news(self, response):
        contentHtml = response.xpath('//*[@id="js_content"]')
        datadate = datetime.datetime.strptime(response.meta['datadate'], '%Y-%m-%d %H:%M:%S')

        public_Id = response.meta['public_Id']
        public_name = public_dict[public_Id]

        contentString1 = ''
        for content in contentHtml:
            if content.xpath('.//text()').extract()<>[] :

                for contentStr in content.xpath('.//text()').extract():
                    contentString1 = contentString1 + contentStr
                contentString1 = contentString1 + '\n'

        item = CM_publicItem()
        item['datadate'] = datadate
        item['news_title'] = response.meta['title']
        item['news_html'] = u''
        item['public_Id'] = public_Id
        item['public_name'] = public_name
        #公众号链接是有时限的，没必要保存
        item['news_contenturl'] = u''
        item['news_imageurl'] = u''
        item['update_dt'] = datetime.datetime.now()
        item['news_content'] = contentString1
        yield item