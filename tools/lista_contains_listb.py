# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_filea', default='in.tsv', type=str)
    parser.add_argument('--in_fileb', default='in.tsv', type=str)
    args = parser.parse_args()
    print(args)
    return args


def contains(word, words):
    r = []
    for w in words:
        if word in w:
            r.append(w)
    return list(set(r))


def list_contains(list_a, candidate_words):
    res = []
    for a in list_a:
        match_w = contains(a, candidate_words)
        if match_w:
            res.append((a, match_w))
    return res


if __name__ == '__main__':
    list_a = ['a', 'bb']
    list_b = ['abc', 'bbc', 'cbbd']
    print(list_contains(list_a, list_b))

    args = get_args()
    data_list = []

    words = [i.strip() for i in open(args.in_fileb, 'r', encoding='utf-8').readlines() if i]
    with open(args.in_filea, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            terms = line.split('\t')
            # line = '\t'.join(terms[2:])
            w = terms[0]
            r = list_contains([w], words)
            if r:
                print(line + '\t' + str(r) + '\t' + str(r[0][1][0]))
            else:
                print(line)
