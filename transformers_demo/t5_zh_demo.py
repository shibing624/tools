# -*- coding: utf-8 -*-
from transformers import T5Tokenizer, T5ForConditionalGeneration
import os
#tokenizer = T5Tokenizer.from_pretrained("Langboat/mengzi-t5-base")
#model = T5ForConditionalGeneration.from_pretrained("Langboat/mengzi-t5-base")

#print(model)
#tokenizer.save_pretrained('../../transformers_models/mengzi-t5-base')
#model.save_pretrained(os.path.expanduser('../../transformers_models/mengzi-t5-base'))
# t5 v1.1 无finetune，需要自己finetune模型

import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

article_text = """Videos that say approved vaccines are dangerous and cause autism, cancer or infertility are among those that will be taken down, the company said.  The policy includes the termination of accounts of anti-vaccine influencers.  Tech giants have been criticised for not doing more to counter false health information on their sites.  In July, US President Joe Biden said social media platforms were largely responsible for people's scepticism in getting vaccinated by spreading misinformation, and appealed for them to address the issue.  YouTube, which is owned by Google, said 130,000 videos were removed from its platform since last year, when it implemented a ban on content spreading misinformation about Covid vaccines.  In a blog post, the company said it had seen false claims about Covid jabs "spill over into misinformation about vaccines in general". The new policy covers long-approved vaccines, such as those against measles or hepatitis B.  "We're expanding our medical misinformation policies on YouTube with new guidelines on currently administered vaccines that are approved and confirmed to be safe and effective by local health authorities and the WHO," the post said, referring to the World Health Organization."""

model_name = "csebuetnlp/mT5_multilingual_XLSum"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

input_ids = tokenizer(
    [WHITESPACE_HANDLER(article_text)],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
    max_length=512
)["input_ids"]
print('input_ids:', input_ids)

output_ids = model.generate(
    input_ids=input_ids,
    max_length=84,
    no_repeat_ngram_size=2,
    num_beams=4
)[0]

summary = tokenizer.decode(
    output_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)

print(summary)

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

article_text = """
10月21日晚，朝阳警方发布最新通报：接到群众举报，有人在朝阳某小区卖淫嫖娼。嫖娼人员叫李某迪，39岁，对违法事实供认不讳，已经依法被捕。在发布这条微博之前，平安北京还发布了“预告”：“这个世界的确不止黑白两色，但一定要分清和划清黑与白。这个，绝对不可以错……”没错，这个39岁的李某迪，正是大名鼎鼎的钢琴家李云迪。据网易娱乐报道，有知情人士爆料，李云迪因嫖娼被抓已经不是第一次了，今年上半年就已经被抓了一次，但并未流传开来。知情人还表示，李云迪早年在德国读书的时候，感情经历就十分丰富，在学生当中的口碑并不好。18岁即获肖邦国际钢琴大赛冠军，5次登上春晚，荣获“中国十大青年领袖”等荣誉称号，还是重庆政协常委、全国青联常委、香港青联副主席……虽然李云迪这些年绯闻不断，但“温文尔雅”、“文质彬彬”、“钢琴王子”等关键词始终贯穿着他的前半生，没有人会把“嫖娼”与他结合在一起。
"""

input_ids = tokenizer(
    [WHITESPACE_HANDLER(article_text)],
    return_tensors="pt",
    padding="max_length",
    truncation=True,
    max_length=512
)["input_ids"]

print('input_ids:', input_ids)
output_ids = model.generate(
    input_ids=input_ids,
    max_length=84,
    no_repeat_ngram_size=2,
    num_beams=4
)[0]

summary = tokenizer.decode(
    output_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)

print(summary)

