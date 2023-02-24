# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import argparse

import addressparser


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', default='address_name.csv', type=str, help='input file')
    args = parser.parse_args()
    print(args)
    return args


if __name__ == '__main__':
    args = get_args()
    adds = [line.strip() for line in open(args.input_file, 'r', encoding='utf-8')]
    r = addressparser.transform(adds)
    print(r)
    rs = r.loc[:, ('省', '市')]
    print(rs)
    rs.to_csv('address_res.csv', index=False, sep='\t')
