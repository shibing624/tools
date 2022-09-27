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

def replace_text(text, old_text, new_text):
    text = text.strip()
    if not text:
        return text
    if old_text in text:
        text = text.replace(old_text, new_text)
    return text

if __name__ == '__main__':
    sents = [
        '100730840_书旗小说',
        '小说',
        '课程'
    ]
    print(replace_text(sents[0], sents[1], sents[2]))

    args = get_args()
    data_list = []
    with open(args.in_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            terms = line.split('\t')
            r = replace_text(terms[0], '{{keyword}}', terms[2])
            r = replace_text(r, '{{city}}', '本地')
            l = replace_text(terms[1], '{{keyword}}', terms[2])
            l = replace_text(l, '{{city}}', '本地')
            print(r + '\t' + l)

