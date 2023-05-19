# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from redlines import Redlines

test = Redlines("The quick brown fox jumps over the lazy dog.",
                "The quick brown fox walks past the lazy dog.")
print(test.output_markdown)
