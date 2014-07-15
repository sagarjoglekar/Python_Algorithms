#! /usr/bin/env scapy
import class2

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return ' hello world'

    def __init__(self,val):
    	self.i = val

if __name__ == '__main__':
    obj1 = MyClass(10)
    obj2 = class2.dummyclass(obj1.f())
    
    print obj2.stringtoken()
    #print obj2.fibonacci(41)
    #print obj2.DPfibonacci(1000)
    print obj2.bottomupDPfibonacci(1000)