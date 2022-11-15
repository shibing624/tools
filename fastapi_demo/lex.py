# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import os

import jieba
import jieba.analyse
import jieba.posseg
from loguru import logger
__all__ = ["Lexer"]


class Lexer:
    def __init__(self, custom_dict_path=None):
        self.lexer_model = jieba
        if custom_dict_path:
            try:
                self.lexer_model.load_userdict(custom_dict_path)
            except IOError:
                pwd_path = os.path.abspath(os.path.dirname(__file__))
                custom_dict_path = os.path.join(pwd_path, '../..', custom_dict_path)
                self.lexer_model.load_userdict(custom_dict_path)
        self.lexer_model_analyse = jieba.analyse
        logger.info('model loaded.')

    def posseg(self, text):
        return self.lexer_model.posseg.cut(text)

    def seg(self, text):
        return self.lexer_model.cut(text)

    def check(self, text):
        """
        Args:
            text: I love it
        Returns:
        {
          "text":"I love it",
          "items":[
            {
           "length":1,
           "offset":0,
           "formal":"",
           "item":"I",
           "ne":"p",
           "pos":"n",
           "uri":"",
           "loc_details":[ ],
           "basic_words":["I"]
            },
        }
        """
        result_dict = {"text": text}
        words = self.posseg(text)
        items_list = []
        idx = 0
        for w in words:
            items = dict()
            items["item"] = w.word
            items["pos"] = w.flag
            items['length'] = len(w.word)
            items['offset'] = idx
            idx = len(w.word) + idx
            items['formal'] = ''
            items['ne'] = ''
            items['uri'] = ''
            items['loc_details'] = []
            items['basic_words'] = [w.word]
            items_list.append(items)
        result_dict['items'] = items_list
        return result_dict
