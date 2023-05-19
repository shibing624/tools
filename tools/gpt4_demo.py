# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from gpt4free import forefront

# create an account
token = forefront.Account.create(logging=False)
print(token)
# get a response
for response in forefront.StreamingCompletion.create(
        token=token,
        prompt='who are you?',
        model='gpt-4'):
    print(response.choices[0].text, end='')


def get_gpt4_response(prompt):
    res = ''
    for response in forefront.StreamingCompletion.create(token=token, prompt=prompt, model='gpt-4'):
        res += response.choices[0].text
    return res


sents = """
我能用lightning数据线给安卓手机充电吗？
为什么天空是蓝色的？
如何做披萨？
为什么冥王星被踢出太阳系？
列举太阳系的全部行星
详细说明DNA和RNA的区别
中国的“东北三省”指的是哪里？
经常吃烫的东西会罹患什么病？
盐酸莫西沙星能否用于治疗肺炎？
机场代码KIX代表的是哪个机场？
介绍一下导演张艺谋。
"""
for sent in sents.split('\n'):
    print('Q:', sent)
    print('A:', get_gpt4_response(sent))
    print('-' * 42)
    import time
    time.sleep(3)