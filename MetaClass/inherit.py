#/usr/bin/python3
# -*- coding: utf-8 -*-

class CBase(object):
    def work(self):
        print("base work")

    def run(self):
        print("base run")


base = CBase()
base.run()

class CWorkUnit1(CBase):
    def work(self):
        print("unit1 work")

base1 = CWorkUnit1()
base1.work()
base1.run()

#Need __init__
#1.子类继承父类时，如果__init__方法被重写，可以使用super函数调用父类的__init__方法，否则被改写的__init__方法会覆盖原有的自动继承的__init__方法。 
#2.类的继承，就是子类继承除了构造函数之外的所有的东西，__init__方法不是构造方法（函数）
#3.子类继承父类时，__init__方法被自动继承，并在创建实例时，自动调用。

class CNeedInitBase(object):
    def __init__(self):
        self.data = "CNeedInitBase"

    def printClassName(self):
        print(self.data)

class CNeedInitDirve(CNeedInitBase):
    def __init__(self):
        super().__init__()
        self.DirveData = "gg"

    def printClassName(self):
        print(self.data)
        print(self.DirveData)
 
InitBase = CNeedInitBase()
InitBase.printClassName()

InitDirve = CNeedInitDirve()
InitDirve.printClassName()

#多重继承
'''
当两个基类有方法重名的时候，python3会按照您继承类的从左到右的顺序查找您调用的方法
B2(A2,A1)。在这个例子中，是先找A2，然后再找A1。
'''
class A1(object):
    def func1(self):
        print("A1's func1")
    def func2(self):
        print("A1's func2")

class A2(object):
    def func1(self):
        print("A2's func1")
    def func2(self):
        print("A2's func2")

class B1(A1, A2):
    def func1(self):
        print("B1's func1")

class B2(A2, A1):
    def func2(self):
        print("B2's func2")

b1 = B1()
b1.func1()  #B1's func1
b1.func2()  #A1's func2

b2 = B2()
b2.func1() #A2's func1
b2.func2() #B2's func2

