#!/usr/bin/python3
# -*- coding: utf-8 -*-

srclist = ['where' , 'are', 'you' , 'from' ,'?', '9527', '?']

for item in srclist:
    print(item , end = '  ')

def printlist():
    for index, item in enumerate(srclist):
        print(index , item)

printlist()
srclist.append(" hello 周星驰")

printlist()
srclist.sort()
printlist()

#删除,以及使用下标
print('The first item I will buy is:', srclist[0])
olditem = srclist[0]
srclist.remove(olditem) # 按值删除,当这值不存在列表时会报错
srclist.remove('?') # 按值删除,当这值不存在列表时会报错
del srclist[0]
print('I bought the', olditem)
print('My shopping list is now:', srclist) # 打印:['banana', 'carrot', 'mango', 'rice']

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [10,11,12]

srclist1 = []
srclist1.append(list1)
srclist1.append(list2)
srclist1.append(list3)

print(srclist1)
oldlist = srclist1[0]
del srclist1[0]

print(oldlist)
list2.remove(5)
print(srclist1)

import copy
cpylist = copy.deepcopy(list1)
cpylist.append("1yjd3")
cpylist.remove(4)

print(list1)
print(cpylist)
c = list1
c.append('qwe')
print(c)
print(list1)
print(cpylist)
