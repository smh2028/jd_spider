京东商品评论分布式爬虫

scrapy,scrapy-redis,redis-py组成的scrapy的分布式爬虫，爬取京东搜索结果的商品评论。



# 爬取逻辑

从https://search.jd.com搜索关键字出发，比如搜索耳机，爬取搜索结果的前n页商品信息。

# 反反爬策略

## 随机User-Agent

实现了JdSpiderDownloaderMiddleware，在process_request方法中对每个request都添加了随机的User-Agent，通过fake-userangent库实现。

## 代理ip

todo

# 商品评论信息存储

![1533130803741](C:\Users\smh\AppData\Local\Temp\1533130803741.png)


