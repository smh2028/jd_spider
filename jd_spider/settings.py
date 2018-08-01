# -*- coding: utf-8 -*-

# Scrapy settings for jd_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd_spider'

SPIDER_MODULES = ['jd_spider.spiders']
NEWSPIDER_MODULE = 'jd_spider.spiders'

MONGO_URI = 'localhost'
MONGO_DB = 'jd_goods'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jd_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False




# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9,ig;q=0.8',
#     'Connection': 'keep-alive',
#     'Cookie': 'pinId=vx3F2gk0h4o; pin=smh2208; unick=smh2208; _tp=GURkv%2B8S4oHLw%2F2ePIv64w%3D%3D; _pst=smh2208; user-key=c7fb0bfd-cd42-4eaa-a239-1187665972c3; xtest=1976.cf6b6759; qrsc=3; ipLoc-djd=19-1607-47388-0.352895607; ipLocation=%u5E7F%u4E1C; __jdu=15280283429551521419482; cn=1; PCSYCityID=1607; TrackID=1su4e7T2mnezchCKLQnr0D-6P_GVCxYEX5-1KpJX_FdXVBdzjrC79ffklSPOaijD_GQf7665hlGGLtSEYCl1plS5Ad5KNRr8T_dAWDI2o6WE; __jda=122270672.15280283429551521419482.1528028343.1530992065.1531027430.25; __jdc=122270672; __jdv=122270672|media|-|cpc|media_8_58871498_s1519954444c7a6e9722.94490214|1531027430080; shshshfpb=27f14f3132ca04fec9e619e97bab48f9d5b1437570a2374c54a13dd922; shshshfpa=b4d1da1e-37b8-0e52-60dd-f5f13140b04f-1531027431; shshshfp=b0f605fea5611600dac87586acaf0386; rkv=V0800; 3AB9D23F7A4B3C9B=HKNHOXPMCZENEPRAIVEFCVKMWDK4PSFO5RCCZJQYV4E4KAUEJ555KY5R5XYE5ZLIGDSVSOJGTQ4A5SDCHAYKTIUDQM; __jdb=122270672.10.15280283429551521419482|25.1531027430; shshshsID=c3c02c7dc79dcecf8fd0385a1e2973a2_10_1531030720620',
#     'Refer':'Referer: https://search.jd.com/Search?keyword=%E8%80%B3%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%80%B3%E6%9C%BA&page=1&s=1&click=0',
#     'Host': 'search.jd.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest'
# }
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jd_spider.middlewares.JdSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jd_spider.middlewares.JdSpiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html

MYEXT_ENABLED=True      # 开启扩展
IDLE_NUMBER=3           # 配置空闲持续时间单位为 360个 ，一个时间单位为5s

EXTENSIONS = {
   # 'scrapy.extensions.telnet.TelnetConsole': None,
   'jd_spider.extensions.RedisSpiderSmartIdleClosedExensions': 500,
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'jd_spider.pipelines.MongoPipeline': 300,
}

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

SCHEDULER = "scrapy_redis.scheduler.Scheduler"  #启用Redis调度存储请求队列
SCHEDULER_PERSIST = True    #不清除Redis队列、这样可以暂停/恢复 爬取
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #确保所有的爬虫通过Redis去重
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_HOST = 'localhost'  # 也可以根据情况改成 localhost
REDIS_PORT = 6379
REDIS_PARAMS = {
   # 'password': 在此设置密码,
   'db': 2
}
REDIS_URL = None



