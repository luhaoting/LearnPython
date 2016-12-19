#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random

#srcList = [random.randrange(0, 100, 1) for x in range(0, 10)]

srcList = [4,6,7,9,5,3,1,2]
def QuickSort(list, left, right):
    #pivot = list[left] # 起始点作为参考点 
    pivot = list[int((right + left) // 2) ] #也可以选取中间点 这个地方一开始使用了减法 找了好久 脑子进水了
    subleft = left
    subright = right
    while subleft <= subright:
        while list[subleft] < pivot:
            subleft += 1
        while pivot < list[subright]:
            subright -= 1
        if subleft <= subright: # == 的时候需要 偏移下标 .. []...中间的值已经在正确的位置了不需要加入分区递归
            tmp = list[subright]
            list[subright] = list[subleft]
            subright -= 1
            list[subleft] = tmp
            subleft += 1
    if left < subright: # 递归左区间
        QuickSort(list, left, subright)
    if subleft < right:
        QuickSort(list, subleft, right)
    return list


print("Src : ", srcList)
QuickSort(srcList, 0, len(srcList) - 1)
print("Sort Result ", srcList)