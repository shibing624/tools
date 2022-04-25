# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from enum import Enum, unique


class EncoderType(Enum):
    FIRST_LAST_AVG = 0
    LAST_AVG = 1
    CLS = 2
    POOLER = 3
    MEAN = 4

    def __str__(self):
        return self.name

    @staticmethod
    def from_string(s):
        try:
            return EncoderType[s]
        except KeyError:
            raise ValueError()

if __name__ == '__main__':

    s = 'FIRST_LAST_AVG'
    print(EncoderType[s])
    print(EncoderType.FIRST_LAST_AVG)
    k = lambda x: EncoderType[x]
    v = k('FIRST_LAST_AVG')
    print(type(v), v)
    print(k('LAST_AVG'))
    m = EncoderType.from_string('FIRST_LAST_AVG')
    print(m)