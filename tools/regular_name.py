# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import argparse
import re


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_file', default='in.tsv', type=str,
                        help='file path')
    args = parser.parse_args()
    print(args)
    return args

def regular_text(text):
    text = text.strip()
    if not text:
        return text
    if '_' in text:
        text = text.split('_', 1)[1]
    if '-' in text:
        text = text.split('-', 1)[0]
    if '：' in text:
        text = text.split('：', 1)[0]
    if ':' in text:
        text = text.split(':', 1)[0]
    return text

if __name__ == '__main__':
    sents = [
        '100730840_书旗小说',
        '100783983_安居客一二手房新房租房商铺',
        '100884650_联通手机营业厅(官方版)',
        '捕鱼大作战-真人千炮捕鱼游戏王者',
        '不休战队：赛博朋克世界',
        '415606289_安居客-二手房、新房、租房的找房助手',
        '书旗小说',
    ]
    for i in sents:
        print(regular_text(i))

    args = get_args()
    data_list = []
    with open(args.in_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            r = regular_text(line)
            print(r)
