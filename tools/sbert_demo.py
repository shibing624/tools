# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from sentence_transformers import SentenceTransformer, util
import pandas as pd
from sklearn.preprocessing import normalize

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
print(model)
sentence_embeddings = model.encode(['hello world', 'hi what is?', 'who are you ?', '你是谁 ？'])
print(len(sentence_embeddings))

# Two lists of sentences
sentences1 = ['The cat sits outside',
              'A man is playing guitar',
              'The new movie is awesome',
              '鼻炎怎么治疗',
              '痔疮怎么治疗',
              '得了皮肤病怎么办',
              '瘙痒怎么办',
              '点击咨询_{酒糟鼻好治吗}?赣州中研皮肤病医院 {酒糟鼻好治吗}?酒渣鼻,又称玫瑰痤疮.其常见发病部位为面部中间,鼻尖,鼻翼. 治疗多为对症性,目前治疗方法主要分为:①系统治疗②局部治疗③物理和手术治疗.',
              '{鼻子发炎怎么治}_2020好的鼻子发炎治疗方法,已验证 {鼻子发炎怎么治} 主诉:经常性鼻塞,流黄粘鼻涕,睡不好怎么办,医生提醒:对症治疗是关键, 专科排除鼻子发炎难题,鼻子发炎患者必选医院,立刻点击预约不排队.',
              '[医保]萎缩性鼻发炎的手术方法, 南昌博大,对症治疗,在德国STORZ鼻内窥镜下手术, 找准病因,制定个性化诊疗方案,手术,物理,心理治疗相结合. ',
              '{哪治痔疮好}(点击查看)一个{祛痔疮方法}! 治痔疮的方法?得了痔疮怎么办,用这个办法后,我的痔疮得到了缓解',
              '{痣疮图}?痣疮如何更好的治疗? {痣疮图}?痣疮症状图片?南充肛肠医院,,肛肠专科医院!治痣疮更专业. ',
              '{寒冷性皮肤病的治疗} 乘风中医院 {皮肤病怎么治疗}?大庆乘风中医院!大庆皮肤病的治疗方法有哪些?',
              '{陕西治癫医院}癫发作能治吗!',
              '<晋城>{去除阴虱}?阴虱引起的瘙痒怎么办?',
              '鼻炎酒糟鼻难受',
              '拉斯蒂在哪？小熊猫从国家动物园消失',
              '瑞典驻利比亚班加西领事馆发生汽车炸弹袭击，无人员伤亡',
              ]

sentences2 = ['The dog plays in the garden',
              'A woman watches TV',
              'The new movie is so great',
              '点击咨询_{酒糟鼻好治吗}?赣州中研皮肤病医院 {酒糟鼻好治吗}?酒渣鼻,又称玫瑰痤疮.其常见发病部位为面部中间,鼻尖,鼻翼. 治疗多为对症性,目前治疗方法主要分为:①系统治疗②局部治疗③物理和手术治疗.',
              '{鼻子发炎怎么治}_2020好的鼻子发炎治疗方法,已验证 {鼻子发炎怎么治} 主诉:经常性鼻塞,流黄粘鼻涕,睡不好怎么办,医生提醒:对症治疗是关键, 专科排除鼻子发炎难题,鼻子发炎患者必选医院,立刻点击预约不排队.',
              '[医保]萎缩性鼻发炎的手术方法, 南昌博大,对症治疗,在德国STORZ鼻内窥镜下手术, 找准病因,制定个性化诊疗方案,手术,物理,心理治疗相结合. ',
              '{哪治痔疮好}(点击查看)一个{祛痔疮方法}! 治痔疮的方法?得了痔疮怎么办,用这个办法后,我的痔疮得到了缓解',
              '{痣疮图}?痣疮如何更好的治疗? {痣疮图}?痣疮症状图片?南充肛肠医院,,肛肠专科医院!治痣疮更专业. ',
              '{寒冷性皮肤病的治疗} 乘风中医院 {皮肤病怎么治疗}?大庆乘风中医院!大庆皮肤病的治疗方法有哪些?',
              '{陕西治癫医院}癫发作能治吗!',
              '<晋城>{去除阴虱}?阴虱引起的瘙痒怎么办?',
              '失踪小熊猫安全返回国家动物园',
              '汽车炸弹击中瑞典驻班加西领事馆，无人受伤',
              ]

# Compute embedding for both lists
embeddings1 = model.encode(sentences1)
embeddings2 = model.encode(sentences2)
print(embeddings1.shape)

# Compute cosine-similarits
cosine_scores = util.cos_sim(embeddings1, embeddings2)

# Output the pairs with their score
for i in range(len(sentences1)):
    for j in range(len(sentences2)):
        print("Score: {:.4f} \t {} \t {}".format(
            cosine_scores[i][j], sentences1[i], sentences2[j]))
print()
