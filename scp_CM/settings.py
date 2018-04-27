# -*- coding: utf-8 -*-

# Scrapy settings for scp_CM project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scp_CM'

SPIDER_MODULES = ['scp_CM.spiders']
NEWSPIDER_MODULE = 'scp_CM.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scp_CM (+http://www.yourdomain.com)'

SER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY=0.5
SPIDER_MIDDLEWARES = {
   'spiderlib.middlewares.IndexPageSaveMiddleware': 300,
}
EXTENSIONS = {
   'spiderlib.extensions.WriteEtlLog': 300,
}
ITEM_PIPELINES = {
   'scp_CM.pipelines.scp_CM_PublicPipleline': 300,
}
LOG_LEVEL = 'INFO'

DATABASE = 'oracle://stg:stg123@10.6.0.94:1521/?service_name=db'
dbconnect='10.6.0.94:1521/db'
dbusername='stg'
dbpassword='stg123'

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scp_CM.pipelines.ScpCmPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
