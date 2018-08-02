京东商品评论分布式爬虫

scrapy,scrapy-redis,redis-py组成的scrapy的分布式爬虫，爬取京东搜索结果的商品评论。

# 下载安装

## 下载源码

git clone https://github.com/smh2028/jd_spider.git

## 安装依赖

pip install -r requirements.txt

## 启动

配置redis start-urls

`redis-cli

LPUSH start_urls https://search.jd.com`

在jd_spider/jd_spider/spiders目录下

`scrapy crawl jd_sp`

# 爬取逻辑

从https://search.jd.com搜索关键字出发，比如搜索耳机，爬取搜索结果的前n页商品信息。

# 反反爬策略

## 随机User-Agent

实现了JdSpiderDownloaderMiddleware，在process_request方法中对每个request都添加了随机的User-Agent，通过fake-userangent库实现。

## 代理ip

todo

# 商品评论信息存储



# Requirements

见requirements.txt