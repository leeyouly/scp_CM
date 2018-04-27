# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scp_CM.data import ImportCM_publicStorage
from scp_CM.items import CM_publicItem
from scrapy.utils.project import get_project_settings

class ScpCmPipeline(object):
    def process_item(self, item, spider):
        return item


class scp_CM_PublicPipleline(object):
    def __init__(self):
        self.storage = ImportCM_publicStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, CM_publicItem):
            if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')

        return item
