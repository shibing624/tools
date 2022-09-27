# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import argparse
from loguru import logger
import json


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_file', default='in.tsv', type=str)
    parser.add_argument('--src_col', default=0, type=int)
    parser.add_argument('--trg_col', default=1, type=int)
    args = parser.parse_args()
    print(args)
    return args


def sim_text_chars(text1, text2):
    if not text1 or not text2:
        return 0.0
    same = set(text1) & set(text2)
    m = len(same)
    n = len(set(text1)) if len(set(text1)) > len(set(text2)) else len(set(text2))
    return m / n


def count_matches(labels, preds):
    logger.debug(f"labels: {labels[:10]}")
    logger.debug(f"preds: {preds[:10]}")
    match = sum([sim_text_chars(label, pred) for label, pred in zip(labels, preds)]) / len(labels)
    logger.debug(f"match: {match}")
    return match


if __name__ == '__main__':
    print(sim_text_chars('你好', '你好啊'))
    args = get_args()
    with open(args.in_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            items = line.split('\t')
            if len(items) < 2:
                continue
            sim_score = sim_text_chars(items[args.src_col], items[args.trg_col])
            print(f"{items[args.src_col]}\t{items[args.trg_col]}\t{sim_score}")
