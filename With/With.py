#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
'''
with obj 语句在控制流程进入和离开其后的相关代码中，允许对象obj管理所发生的事情。

执行 with obj 语句时，它执行 obj.__enter__() 方法来指示正在进入一个新的上下文。
当控制流离开该上下文的时候，它就会执行 obj.__exit__(type, value, traceback)。
'''

#with 语法糖 只能作用于实现了 __enter__() 和 __exit__()的object

class A:
    pass

class test:
    def __enter__(self):
        print("enter...")
        return 1

    def __exit__(self,*args):
        print("exit...")
        return True

'''
AttributeError: __exit__
with A() as a:
    print("a is not the result of test(), it is __enter__ returned")
    print("a is 1, yes, it is {0}".format(a))
    raise NameError("Hi there")
    print("Never here")
'''

with test() as t:
    print("t is not the result of test(), it is __enter__ returned")
    print("t is 1, yes, it is {0}".format(t))
    #raise NameError("Hi there")
    print("Never here")


