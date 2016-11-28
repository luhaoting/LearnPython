#!/usr/python

class ObjectCreator(object):
    pass
    

my_object = ObjectCreator()
print(my_object)

print(ObjectCreator)

def echo_hello11(self):
    print("hex")



Foo = type('Foo',(),{'bar':True, 'echo_hello': echo_hello11})

f = Foo()
print(f)

f.echo_hello()

def echo_hello(self):
    print("hello!")


Foo.echo_hello = echo_hello
f.echo_hello()


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''
    返回一个类对象，所有属性都转成大写
    '''
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val
            
    return type(future_class_name, future_class_parents, uppercase_attr)

class UpperCastAttr(type):
    def __new__(cls, name, bases, attrs):
        return upper_attr(name, bases, attrs)


class BigAttr(metaclass=UpperCastAttr):
    def __init(self, **kw):
        super(Model, self).__init__(**kw)

    def print_hello(slef):
        print("class big hello")


big = BigAttr()
big.PRINT_HELLO() #英吹思婷
