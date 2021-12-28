# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import json
a = {1:'1',2:'2',3:'赌博'}
b = json.dumps(a, ensure_ascii=False,)
print(b)
b = json.dumps(a)
print(b)

import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

text = json.loads(jsonData)
print(text)

a = """{"1": "1", "2": "2", "3": "\u8d4c\u535a"}"""
c = json.loads(b)
print(b)

k = """
{"model_result": {"ad_softtext": {"label": "\u8f6f\u6587", "lable_prob": 0.8659609433307157}}, "accountid": "23139905", "groupid": "1909776761", "id": "15224573408", "text": "\u5b69\u5b50\u5f97\u4e86\u62bd\u52a8\u75c7\u4e0d\u53ef\u6015,\u5173\u952e\u662f\u9009\u5bf9\u65b9\u6cd5! \u5b69\u5b50\u62bd\u52a8\u75c7,\u7ecf\u5e38\u7728\u773c,\u8038\u80a9,\u6e05\u55d3\u5b50,\u6447\u5934\u6643\u8111,\u8eab\u4f53\u4e0d\u7531\u81ea\u4e3b\u62bd\u52a8\u7b49, \u540e\u6765\u7528\u4e86\u8fd9\u4e2a\u65b9\u6cd5,\u73b0\u5728\u5b69\u5b50\u62bd\u52a8\u75c7\u597d\u591a\u4e86,\u503c\u5f97\u8bd5\u8bd5!", "visiturl": "http://renai.zhengdianlinghua.com/", "status": "-1", "memo": "50012", "date": "2021-11-01 11:03:35.0"}
"""
print(json.loads(k))