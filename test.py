# -*- coding: utf-8 -*-
'''
@author  : smh2208
@software: PyCharm
@file    : test.py
@time    : 2018/7/8 14:04
@desc    :
'''

# search_result_url = 'https://search.jd.com/Search?keyword=%E8%80%B3%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&' \
#                         'wq=%E8%80%B3%E6%9C%BA&page={0}&s={1}&click=0'
#
# for page in range(1, 6,2):
#     url = search_result_url.format(page, 1 + int(56 * (page - 1) / 2))
#     print(url)

# s = 'https://search.jd.com/s_new.php?keyword=%E8%80%B3%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%80%B3%E6%9C%BA&page=2&s=27&scrolling=y&log_id=1531030888.63562&tpl=3_M&show_items=10100955487,3563660,5463278,5051645,5793568,4406782,10650398425,2807801,2986763,6356969,5561324,2930414,13089190682,5340538,5934907,5180591,3262461,6004883,6471490,5487385,3487483,173137,4635250,2117728,2952697,5046941,3618695,4167081,25015976606,3599558,'
# print(s.strip(','))

hearders = {
        # 'Accept': '*/*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,ig;q=0.8',
        # 'Connection': 'keep-alive',
        # 'Cookie':'pinId=vx3F2gk0h4o; pin=smh2208; unick=smh2208; _tp=GURkv%2B8S4oHLw%2F2ePIv64w%3D%3D; _pst=smh2208; xtest=1976.cf6b6759; qrsc=3; ipLoc-djd=19-1607-47388-0.352895607; ipLocation=%u5E7F%u4E1C; __jdu=15280283429551521419482; PCSYCityID=1607; TrackID=1su4e7T2mnezchCKLQnr0D-6P_GVCxYEX5-1KpJX_FdXVBdzjrC79ffklSPOaijD_GQf7665hlGGLtSEYCl1plS5Ad5KNRr8T_dAWDI2o6WE; __jda=122270672.15280283429551521419482.1528028343.1530992065.1531027430.25; __jdc=122270672; __jdv=122270672|media|-|cpc|media_8_58871498_s1519954444c7a6e9722.94490214|1531027430080; rkv=V0800; user-key=545aac19-ccc9-4a77-a5f8-09870f2eafbb; cn=0; __jdb=122270672.18.15280283429551521419482|25.1531027430; shshshfp=a7b65c2eb9689050e574820b492d5bfc; shshshfpa=dd94c52b-97fc-412a-bc1a-a0ac53c82bbb-1531033507; shshshfpb=27f14f3132ca04fec9e619e97bab48f9d5b1437570a2374c54a13dd922; shshshsID=ece632f5dc2242eeda06dfe6cc5ebc24_1_1531033507588',
        'Referer': 'https://search.jd.com/Search?keyword=%E8%80%B3%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%80%B3%E6%9C%BA&page=1&s=1&click=0',
        # 'Host': 'search.jd.com',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        # 'X-Requested-With': 'XMLHttpRequest'
    }
print(hearders['Referer'])
h = hearders.copy()
h['Referer'] = 's'
print(h)
print(hearders)
import logging
logging._