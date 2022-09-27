# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
format:

"""

import sys
import json

for line in sys.stdin:
    line = line.strip('\n')
    terms = line.split('\t')
    name = terms[4]
    info = terms[11]
    info_dict = json.loads(info)
    product_word = info_dict.get('productWord', '')
    brand_word = info_dict.get('brandWord', '')
    if product_word or brand_word:
        print('%s\t%s\t%s' % (name, product_word, brand_word))
