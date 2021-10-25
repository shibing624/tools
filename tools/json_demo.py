# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import json
a = {1:'1',2:'2',3:'赌博'}
b = json.dumps(a, ensure_ascii=False,)
print(b)
