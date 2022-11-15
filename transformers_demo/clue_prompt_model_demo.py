# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("ClueAI/PromptCLUE-base")
model = AutoModelForSeq2SeqLM.from_pretrained("ClueAI/PromptCLUE-base")
# 修改colab笔记本设置为gpu，推理更快
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


def preprocess(text):
    return text.replace("\n", "_")


def postprocess(text):
    return text.replace("_", "\n")


def answer(text, sample=False, top_p=0.6):
    '''sample：是否抽样。生成任务，可以设置为True;
       top_p：0-1之间，生成的内容越多样、
    '''
    text = preprocess(text)
    encoding = tokenizer(text=[text], truncation=True, padding=True, max_length=768, return_tensors="pt").to(device)
    if not sample:  # 不进行采样
        out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_length=128, num_beams=4,
                             length_penalty=0.6)
    else:  # 采样（生成）
        out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_length=128,
                             do_sample=True, top_p=top_p)
    out_text = tokenizer.batch_decode(out["sequences"], skip_special_tokens=True)
    return postprocess(out_text[0])


if __name__ == '__main__':
    texts = [
        """情感分析：
            这个看上去还可以，但其实我不喜欢
            选项：积极，消极
            答案：""",
        """下面句子是否表示了相同的语义：
        文本1：糖尿病腿麻木怎么办？
        文本2：糖尿病怎样控制生活方式
        选项：相似，不相似
        答案：""",
        """问题生成：
        中新网2022年9月22日电 22日，商务部召开例行新闻发布会，商务部新闻发言人束珏婷表示，今年1-8月，中国实际使用外资1384亿美元，增长20.2%；其中，欧盟对华投资增长123.7%(含通过自由港投资数据)。这充分表明，包括欧盟在内的外国投资者持续看好中国市场，希望继续深化对华投资合作。
        答案：""",
        """指代消解：
        段落：
        少平跟润叶进了她二爸家的院子，润生走过来对他（代词）说：“我到宿舍找了你两回，你到哪里去了？”
        问题：代词“他”指代的是？
        答案：""",
        """抽取关键词：
        当地时间21日，美国联邦储备委员会宣布加息75个基点，将联邦基金利率目标区间上调到3.00%至3.25%之间，符合市场预期。这是美联储今年以来第五次加息，也是连续第三次加息，创自1981年以来的最大密集加息幅度。
        关键词： """,
        """文字中包含了怎样的情感：
        超可爱的帅哥，爱了。。。
        选项：厌恶，喜欢，开心，悲伤，惊讶，生气，害怕
        答案：""",
        """文本纠错：
        你必须服从命令，不要的考虑。你的思想被别人手下来。
        答案：""",
        """文本纠错：
        少先队员应该为老人让坐。
        答案：""",
        """问答：
        问题：阿里巴巴的总部在哪里?
        答案：""",
        """问答：
        问题：姚明多高?
        答案：""",
        "生成与下列文字相同意思的句子： 长期通胀前景在今天可能不确定性更大。 答案：",
        "改写： 长期通胀前景在今天可能不确定性更大。 答案：",
    ]
    for text in texts:
        print(answer(text))
