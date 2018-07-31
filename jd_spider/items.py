# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class GoodsItem(scrapy.Item):
    gid = Field()
    # comments = Field()
    productName = Field()
    id = Field()
    userLevelName = Field()
    commentTime = Field()
    content = Field()
    score = Field()
    userClientShow = Field()



class GoodsSpiderLoader(ItemLoader):
    default_item_class = GoodsItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()

