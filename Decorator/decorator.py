#!/usr/bin/python3
# -*- coding: utf-8 -*-

#这种写法 输出
#this is decoratorNoparam
#this is func function
#this is func function
#this is func function
#this is func function
#this is decoratorOneparam
#input is [help!]

#但是 why！？

'''
装饰器的本质：语法糖

def decoratorOneparam(func):
    def wrapped(*args, **kwargs):
        print("this is decoratorOneparam")
        func(*args, **kwargs)
    return wrapped


@decoratorOneparam
def funcstr(strinput):
    print("input is [%s]" % strinput)

funcstr("help!")

本质调用了 decoratorOneparam(funcstr)

将funcstr的函数对象 封装入wrapped函数对象中 而decoratorOneparam 本身返回了wrapped对象，
将funcstr 函数包裹在wrapped 对象中。
在单纯调用funcstr 的时候 

根据 闭包&LEGB法则

Local - 本地函数(show_filename)内部，通过任何方式赋值的，而且没有被global关键字声明为全局变量的filename变量；
Enclosing - 直接外围空间(上层函数wrapper)的本地作用域，查找filename变量(如果有多层嵌套，则由内而外逐层查找，直至最外层的函数)；
Global - 全局空间(模块enclosed.py)，在模块顶层赋值的filename变量；
Builtin - 内置模块(__builtin__)中预定义的变量名中查找filename变量；

根据LEGB法则，解释器将搜索几个作用域，并最终在(Enclosing层)decoratorOneparam函数的本地作用域中找到命名为“funcstr”的func函数对象；


'''

'''
def decoratorNoparam(func):
    def wrapped()
        print("this is decoratorNoparam")
        func()
    return wrapped
'''
def decoratorOneparam(func):
    def wrapped(*args, **kwargs):
        print("this is decoratorOneparam")
        func(*args, **kwargs)
    return wrapped


def decoratorNoparam(func):
    print("this is decoratorNoparam")
    func()
    return func

@decoratorNoparam
def func():
    print("this is func function")

@decoratorOneparam
def funcstr(strinput):
    print("input is [%s]" % strinput)

'''
#这个函数可以屏蔽 Enclosing 区域的 funcstr 函数的查询  导致装饰器失效
def funcstr(strinput):
    print("fff is [%s]" % strinput)
'''
func()
func()
funcstr("help!")

