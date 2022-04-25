# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import pygtrie

t = pygtrie.StringTrie()
t['foo'] = 'Foo'
t['foo/bar'] = 'Bar3'
t['foo/bar/baz'] = 'Baz2'
t['bar/baz'] = 'Baz1'
t['r/baz'] = 'Baz4'
t['r/ba'] = 'Baz4'
t['foor/bz'] = 'Baz4'
t['foor'] = 'Baz4'
print(t.keys())
print(t.longest_prefix('foo/bar/baz/qux'))
print(t.longest_prefix('foo/bar/'))
