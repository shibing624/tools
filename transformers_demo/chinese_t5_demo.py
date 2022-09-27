# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from transformers import BertTokenizer, T5ForConditionalGeneration, Text2TextGenerationPipeline

tokenizer = BertTokenizer.from_pretrained("uer/t5-small-chinese-cluecorpussmall")
model = T5ForConditionalGeneration.from_pretrained("uer/t5-small-chinese-cluecorpussmall")
text2text_generator = Text2TextGenerationPipeline(model, tokenizer)
r = text2text_generator("中国的首都是extra0京", max_length=50, do_sample=False)
print(r)

# from transformers import BertTokenizer, MT5ForConditionalGeneration, Text2TextGenerationPipeline
#
# tokenizer = BertTokenizer.from_pretrained("uer/t5-v1_1-small-chinese-cluecorpussmall")
# model = MT5ForConditionalGeneration.from_pretrained("uer/t5-v1_1-small-chinese-cluecorpussmall")
# text2text_generator = Text2TextGenerationPipeline(model, tokenizer)
# r = text2text_generator("中国的首都是extra0京", max_length=50, do_sample=False)
# print(r)

sents = [
    "中国的首都是extra0京",
    "明月几时有，extra0问青天，不知extra1，今夕是何年？我欲extra2归去，又恐琼楼玉宇，高处extra3；起舞extra4清影，何似在人间。",  # 完形填空
    "识别该句子的情感倾向：这趟北京之旅我感觉很不错。",  # 情感分析
    "下面是一则什么新闻？八个月了，终于又能在赛场上看到女排姑娘们了。",  # 主题分类
    "阅读理解：特朗普与拜登共同竞选下一任美国总统。根据上述信息回答问题：特朗普是哪国人？",  # 阅读理解
    "少先队员extra0该为老人让extra1",  # 文本纠错
]

r = text2text_generator(sents, max_length=50, do_sample=False)
for res, sent in zip(r, sents):
    print(sent, res)

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# tokenizer = AutoTokenizer.from_pretrained("lemon234071/t5-base-Chinese")
# model = AutoModelForSeq2SeqLM.from_pretrained("lemon234071/t5-base-Chinese")
# text2text_generator = Text2TextGenerationPipeline(model, tokenizer)
# r = text2text_generator("中国的首都是extra0京", max_length=50, do_sample=False)
# print(r)

from transformers import T5Tokenizer, T5ForConditionalGeneration
tokenizer = T5Tokenizer.from_pretrained("Langboat/mengzi-t5-base")
model = T5ForConditionalGeneration.from_pretrained("Langboat/mengzi-t5-base")

print(model)
text2text_generator = Text2TextGenerationPipeline(model, tokenizer)
sents = [
    "中国的首都是extra0京",
    "明月几时有，extra0问青天，不知extra1，今夕是何年？我欲extra2归去，又恐琼楼玉宇，高处extra3；起舞extra4清影，何似在人间。",  # 完形填空
    "识别该句子的情感倾向：这趟北京之旅我感觉很不错。",  # 情感分析
    "下面是一则什么新闻？八个月了，终于又能在赛场上看到女排姑娘们了。",  # 主题分类
    "阅读理解：特朗普与拜登共同竞选下一任美国总统。根据上述信息回答问题：特朗普是哪国人？",  # 阅读理解
    "少先队员extra0该为老人让extra1",  # 文本纠错
]

r = text2text_generator(sents, max_length=50, do_sample=False)
for res, sent in zip(r, sents):
    print(sent, res)

