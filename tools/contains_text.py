# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import argparse
import re


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed_file', default='in1.tsv', type=str, help='file path')
    parser.add_argument('--in_file', default='in2.tsv', type=str, help='file path')
    args = parser.parse_args()
    print(args)
    return args


def contains_text(text, sub_text):
    res = ''
    text = text.strip()
    if not text:
        return res
    if sub_text in text:
        res = text
    return res


if __name__ == '__main__':
    print(contains_text('1001_书旗小说', '小说'))

    args = get_args()
    seeds = set()
    with open(args.in_file1, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            terms = line.split('\t')
            seeds.add(terms[0])
    print('seeds:', len(seeds))

    with open(args.in_file1, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            terms = line.split('\t')
            name = terms[0]
            flag = False
            for i in seeds:
                if contains_text(name, i):
                    print(name, i)
                    flag = True
                    break
            if not flag:
                print(name, '')
