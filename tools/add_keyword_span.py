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
                        help='Transformers model model or path')
    args = parser.parse_args()
    print(args)
    return args


def del_matcher(text):
    text = text.replace('{', '').replace('}', '')
    return text


def replace_with_keyword_span(text, fill_text='{{keyword}}'):
    span = re.findall("{(.*?)}", text)
    if span:
        key = '{' + span[0] + '}'
        text = text.replace(key, fill_text)
    else:
        text = text
    return text, span


if __name__ == '__main__':
    txt = '《1334》qasdfa《23423》{鸿蒙圣墟}-官方'
    print(replace_with_keyword_span(txt))
    print(del_matcher(txt))

    args = get_args()
    data_list = []
    with open(args.in_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            t, r = replace_with_keyword_span(line)
            if r:
                print(t)
