# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import pypinyin

a = pypinyin.pinyin('中', style=pypinyin.Style.TONE3)
print(a)

b = pypinyin.lazy_pinyin('中', style=pypinyin.Style.TONE3)
print(b)

b = pypinyin.lazy_pinyin('中')
print(b)

b = pypinyin.pinyin('中')
print(b)

b = pypinyin.lazy_pinyin('中过123')
print(b)