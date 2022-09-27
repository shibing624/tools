# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import argparse
import json


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_file', default='in.json', type=str)
    parser.add_argument('--src_name', default='source', type=str)
    parser.add_argument('--trg_name', default='target', type=str)
    args = parser.parse_args()
    print(args)
    return args


if __name__ == '__main__':
    args = get_args()
    data_list = []
    data = json.load(open(args.in_file, 'r', encoding='utf-8'))
    for item in data:
        print(item[args.src_name] + '\t' + item[args.trg_name])
