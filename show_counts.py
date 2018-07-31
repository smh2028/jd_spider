# -*- coding: utf-8 -*-
'''
@author  : smh2208
@software: PyCharm
@file    : show_counts.py
@time    : 2018/7/8 21:57
@desc    :
'''
import pymongo

cl = pymongo.MongoClient('localhost',27017)
db = cl['jd_goods']
co = db['GoodsItem']
#60*10*10就是10条数据
print(co.find().count())