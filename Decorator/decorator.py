#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
def decoratorNoparam(func):
    print("this is decoratorNoparam")
    func()
    return func

这种写法 输出
this is decoratorNoparam
this is func function
this is func function
this is func function
this is func function
this is decoratorOneparam
input is [help!]

但是 why！？

'''

def decoratorNoparam(func):
    def wrapped()
        print("this is decoratorNoparam")
        func()
    return wrapped

def decoratorOneparam(func):
    def wrapped(*args, **kwargs):
        print("this is decoratorOneparam")
        func(*args, **kwargs)
    return wrapped

@decoratorNoparam
def func():
    print("this is func function")

@decoratorOneparam
def funcstr(strinput):
    print("input is [%s]" % strinput)


func()
func()
func()
funcstr("help!")

