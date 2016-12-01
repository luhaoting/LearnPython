#!/usr/bin/python3
# -*- coding: utf-8 -*-

def make_repeater(n):
    ''' 注意: lambda 返回的是函数,而不是表达式的值'''
    return lambda s: s*n

numfunc = make_repeater(2)
print(numfunc(152))

strFunc = make_repeater(2)
print(strFunc("rini"))

print((lambda s : s*100)(100))

print((lambda s , n: s*n)(9,19))
