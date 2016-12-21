#!/usr/bin/python3
# -*- coding: utf-8 -*-

print("%(src)s is string fromat" % {'src':"this is"})

print("{0} {1} {2} {3} {4}".format('I', 'like' ,'this','format',"method"))

# 字典参数的输出
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}


print('Jack:{0[Jack]}; Sjoerd:{0[Sjoerd]:10d}; Dcab:{0[Dcab]!r}'.format(table)) #难以理解的写法，或者说 这样写有什么意义

#这才是标准迭代
for name, phone in table.items():
    print('"{0:10}" ==> "{1:10d}"'.format(name, phone))

print('Yes, it contains the string "war"', 's')

delimiter = '; '
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist)) # 打印: Brazil; Russia; India; China

print("192.168.3.3.21.31.3.4".split('.',1)) # 部分分隔,打印:['192', '168.3.3.21.31.3.4']
print("192.168.3.3.21.31.3.4".split('.',3)) # 部分分隔,打印:['192', '168', '3', '3.21.31.3.4']
print("192.168.3.3.21.31.3.4".split('.',5)) # 部分分隔,打印:['192', '168', '3', '3', '21', '31.3.4']