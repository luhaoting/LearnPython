#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
持久化实例对象
'''

import pickle as pick

shoplistfile = 'shop.data'

shoplist = ['apple', 'mango' , 'carrot', 2 , 5]

f = open(shoplistfile , "wb")
pick.dump(shoplist , f)
f.close()

f = open(shoplistfile , "rb")
storedlist2 = pick.load(f)
print(storedlist2)
f.close()

import random
print( random.randint(1, 5) ) # 生成1至5之间的随机整数，结果大于等于1，小于等于5，前一个参数必须小于等于第二个参数
for i in range(5):
    print(i, random.randint(10, 90) ) # 产生 10~90 的随机整数(结果包含 10 和 90)