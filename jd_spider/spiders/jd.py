# -*- coding: utf-8 -*-
# 京东商品评论分布式爬虫
import scrapy
from scrapy.http import Request
import json
from scrapy import cmdline
from scrapy.http.response import urljoin
from urllib.parse import urljoin
import re
import random,os,sys
from time import sleep
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
ffpath = os.path.abspath(os.path.join(fpath,".."))
# print(ffpath)
sys.path.append(ffpath)
from jd_spider.items import GoodsItem
import logging
from scrapy_redis.spiders import RedisSpider

class JdSpider(RedisSpider):
    name = 'jd_sp'
    redis_key = 'start_urls'

    search_result_url = 'https://search.jd.com/s_new.php?keyword=%E8%80%B3%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2' \
                        '&wq=%E8%80%B3%E6%9C%BA&page={0}&s={1}&click=0'
    scroll_url_example = 'https://search.jd.com/s_new.php?keyword=%E8%80%B3%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&' \
                 'wq=%E8%80%B3%E6%9C%BA&page=2&s=27&scrolling=y&log_id=1531030888.63562&tpl=3_M&show_items=' \
                 '5340538,2988013,13491803521,5934907,4215862,3904935,1133876941,1765895881,3866873,12534105241,' \
                 '2986763,14107231664,10839746256,4488645,2768837,10103996040,3618695,10575932237,18186401837,' \
                 '11212347766,11955924339,4488515,5381078,2952697,6004883,1498253,11265018045,3563660,4281170,5463278'
    scroll_url = 'https://search.jd.com/s_new.php?keyword=%E8%80%B3%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&' \
                 'wq=%E8%80%B3%E6%9C%BA&page={0}&s={1}&scrolling=y&log_id=1531030888.63562&tpl=3_M&show_items={2}'
    comments_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv18243&' \
                   'productId={0}&score=0&sortType=5&page={1}&pageSize=10&isShadowSku=0&fold=1'

    search_referer = 'https://search.jd.com/Search?keyword=%E8%80%B3%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=' \
                      '%E8%80%B3%E6%9C%BA&page={}&s={}&click=0'
    headers = {
        # 'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,ig;q=0.8',
        # 'Connection': 'keep-alive',
        # 'Cookie':'pinId=vx3F2gk0h4o; pin=smh2208; unick=smh2208; _tp=GURkv%2B8S4oHLw%2F2ePIv64w%3D%3D; _pst=smh2208; xtest=1976.cf6b6759; qrsc=3; ipLoc-djd=19-1607-47388-0.352895607; ipLocation=%u5E7F%u4E1C; __jdu=15280283429551521419482; PCSYCityID=1607; TrackID=1su4e7T2mnezchCKLQnr0D-6P_GVCxYEX5-1KpJX_FdXVBdzjrC79ffklSPOaijD_GQf7665hlGGLtSEYCl1plS5Ad5KNRr8T_dAWDI2o6WE; __jda=122270672.15280283429551521419482.1528028343.1530992065.1531027430.25; __jdc=122270672; __jdv=122270672|media|-|cpc|media_8_58871498_s1519954444c7a6e9722.94490214|1531027430080; rkv=V0800; user-key=545aac19-ccc9-4a77-a5f8-09870f2eafbb; cn=0; __jdb=122270672.18.15280283429551521419482|25.1531027430; shshshfp=a7b65c2eb9689050e574820b492d5bfc; shshshfpa=dd94c52b-97fc-412a-bc1a-a0ac53c82bbb-1531033507; shshshfpb=27f14f3132ca04fec9e619e97bab48f9d5b1437570a2374c54a13dd922; shshshsID=ece632f5dc2242eeda06dfe6cc5ebc24_1_1531033507588',
        # 'Referer': 'https://search.jd.com/Search?keyword=%E8%80%B3%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq='
        #            '%E8%80%B3%E6%9C%BA&page={}&s={}&click=0',
        # 'Host': 'search.jd.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        # 'X-Requested-With': 'XMLHttpRequest'
    }

    # start_urls = ['https://search.jd.com']

    #要读取的评论页数
    comment_page_num = 100

    def parse(self, response):
        """构造搜索结果的请求"""
        for page in range(1,5,2):
            obvious_url = self.search_result_url.format(page*2-1, self.obvious_page_s(page))
            # print(obvious_url)
            referer = self.search_referer.format(page*2-1, self.obvious_page_s(page))
            self.headers['Referer'] = referer
            yield Request(url=obvious_url, headers=self.headers, callback=self.parse_obvious_page, dont_filter=True,
                          meta={'page': page})

    # def start_requests(self):
    #     '''对关键字发送请求获得搜索结果'''
    #     for page in range(1,3,2):
    #         obvious_url = self.search_result_url.format(page*2-1, self.obvious_page_s(page))
    #         # print(obvious_url)
    #         referer = self.search_referer.format(page*2-1, self.obvious_page_s(page))
    #         self.headers['Referer'] = referer
    #         yield Request(url=obvious_url, headers=self.headers, callback=self.parse_obvious_page, dont_filter=True,
    #                       meta={'page':page})

    def random_delay(self):
        '''随机延时'''
        # delay = 0.5+random.random() * 1
        # sleep(delay)
        pass

    def obvious_page_s(self,page):
        '''生成搜索结果页前30条商品对应的s值'''
        return 1 + int(56* (page - 1) / 2)

    def scroll_page_s(self,page):
        '''生成搜索结果页需要下拉才显示出来的后30条商品对应的s值'''
        return 27+int(48*(page-1))

    # def start_requests(self):
    #     '''对某一个商品，发起查询评论的请求'''
    #     gid = '3904935'
    #     for i in range(self.comment_page_num):  # 10000
    #         url = self.comments_url.format(gid, i)
    #         print('comments url:', url)
    #         self.random_delay()
    #         yield Request(url, self.parse_comments_page, dont_filter=True, meta={'gid': gid})

    def parse_obvious_page(self, response):
        '''解析搜索结果页'''
        goods_list = response.xpath('//li[@class="gl-item"]')
        spu_string = ''
        for goods in goods_list:
            id = goods.xpath('@data-sku').extract_first()
            spu = goods.xpath('@data-spu').extract_first()
            spu_string += spu+','
            goods_url = 'https://item.jd.com/' + id + '.html'
            # print('goods url:',goods_url)
            # self.start_comments_page_request(id,goods_url)
            self.headers['Referer'] = goods_url
            for i in range(self.comment_page_num):#10000
                url = self.comments_url.format(id, i)
                print('comments url:', url)
                self.random_delay()
                yield Request(url, self.parse_comments_page, dont_filter=True,meta={'gid':id})

        #构造出scroll_page的url
        page = response.meta.get('page')
        scroll_url = self.scroll_url.format(page*2,self.scroll_page_s(page),spu_string.strip(','))
        print(scroll_url)
        referer = self.search_referer.format(page * 2 - 1, self.obvious_page_s(page))
        yield Request(scroll_url,self.parse_scroll_page,dont_filter=True)

    def parse_scroll_page(self, response):
        '''解析搜索结果页下拉显示的30条商品信息'''
        goods_list = response.xpath('//li[@class="gl-item"]')
        for goods in goods_list:
            id = goods.xpath('@data-sku').extract_first()
            spu = goods.xpath('@data-spu').extract_first()
            goods_url = 'https://item.jd.com/'+id+'.html'
            self.headers['Referer'] = goods_url
            for i in range(self.comment_page_num):  # 10000
                url = self.comments_url.format(id, i)
                print('comments url:', url)
                self.random_delay()
                yield Request(url, self.parse_comments_page, dont_filter=True,meta={'gid':id})

    def parse_comments_page(self,response):
        print('*'*200)
        print(response.text)
        comments = response.body.decode('gbk')
        jsonComments = comments[27:-2]
        data = json.loads(jsonComments)
        comm = []
        try:
            comm = data.get('comments')
        except:
            # print('NO COMMENTS FOUND')
            logging.error('NO COMMENTS FOUND')
        if not comm:
            print(data)
            print('GET COMMENTS FAILED!*********************************************************')
            logging.log(1,'GET COMMENTS FAILED')
        for i in comm:
            item = GoodsItem()
            item['gid'] = response.meta['gid']
            item['productName'] = i['referenceName']
            item['id'] = i['id']
            item['userLevelName'] = i['userLevelName']
            item['commentTime'] = i['creationTime']
            item['content'] = i['content']
            item['score'] = i['score']
            item['userClientShow'] = i['userClientShow']
            print(item)
            yield item

if __name__ == '__main__':
    cmdline.execute('scrapy crawl jd_sp '.split())