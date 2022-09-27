# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
from collections import OrderedDict
from loguru import logger
import time

baidu_url_prefix = 'https://www.baidu.com/s?ie=UTF-8&wd='

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.16 Safari/537.36",
}


def get_html_baidu(url):
    """
    获取百度搜索的结果
    :param url:
    :return:
    """
    return BeautifulSoup(requests.get(url=url, headers=headers).content, "lxml")


class Engine:
    def __init__(self, topk=3):
        self.topk = topk
        self.contents = OrderedDict()

    def post_process(self, text):
        r = text.replace('\n', '').replace('\ue62b', '').replace('百度快照', '').replace('\ue67d', '').replace('\ue631', '')
        return r

    def search_baidu(self, query):
        """
        通过baidu检索广告，包括百度广告
        :param query:
        :return: list, string
        """
        answer = []
        # 抓取百度前10条的摘要
        soup_baidu = get_html_baidu(baidu_url_prefix + urllib.parse.quote(query))
        if not soup_baidu:
            return answer
        if soup_baidu.title.get_text().__contains__('百度安全验证'):
            logger.warning("爬虫触发百度安全验证")
            return answer
        ad_all = soup_baidu.findAll(class_="c-span12 c-span-last")[:self.topk]
        if ad_all:
            # 广告
            for i in ad_all:
                try:
                    title = i.find(class_="t ec_title _3qzdx3r").text.strip()
                except:
                    title = ''
                try:
                    ideadesc = i.find(class_="ec_desc").text.strip()
                except:
                    ideadesc = ''
                if title and ideadesc:
                    title = self.post_process(title)
                    ideadesc = self.post_process(ideadesc)
                    answer.append(('AD', title, ideadesc))
            return answer
        else:
            # 网页检索结果
            all = soup_baidu.findAll(class_='c-container')[:self.topk]
            for item in all:
                try:
                    title = item.find(class_='c-title t t tts-title').get_text().strip()
                except:
                    title = ''
                try:
                    ideadesc = item.find(class_='c-span9 c-span-last').get_text().strip()
                except:
                    ideadesc = ''
                if title and ideadesc:
                    title = self.post_process(title)
                    ideadesc = self.post_process(ideadesc)
                    answer.append(('WEB', title, ideadesc))
            return answer


if __name__ == '__main__':
    m = Engine()
    # search ADs
    print(m.search_baidu('毛囊炎治疗'))

    app_names = [
        "恋爱记",
        "时雨天气",
        "强力清理大师 - 极速清理手机垃圾的智能专家",
        "趣吧盒子",
        "爱玩实时变声器",
        "超能WiFi管家",
        "随身计步宝",
        "百利恒运动",
    ]
    res = []
    save_file_path = 'baidu_ad.csv'
    with open(save_file_path, 'w', encoding='utf-8') as f:
        for i in app_names:
            rs = m.search_baidu(i + ' APP')
            time.sleep(1.5)
            print(rs)
            for r in rs:
                if r:
                    f.write('\t'.join((i, r[0], r[1], r[2])) + '\n')
                    res.append((i, r[0], r[1], r[2]))
                else:
                    f.write('\t'.join((i, r[0], r[1], r[2])) + '\n')
                    res.append((i, '', '', ''))
    logger.info(f'Result size: {len(res)}')
