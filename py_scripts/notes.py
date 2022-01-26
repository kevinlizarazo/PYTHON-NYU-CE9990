#!/usr/bin/env python

"""
an object has two main aspects.
1. it holds its own data
2. it has functionality which is specific to its type

our objects must be able to do the following
1. hold its own data
2. call methods specific to its class

steps to creating a class
1. class block names the class.   #class MyClass(object):
2. calling class by name returns a new object.  #x = MyClass() 
3. setting attribute values in the object can be done arbitrarily
    myobj.attr = value
4. reading attribute values in the object can be done by naming the attribute
    y = myobj.attr    # 'value'

methods can be called by defining them in the class and 
calling them on the object which is... x.dothismethod()

what is self? self is the object. 
when a method is called on an object, the object is implicitly
passed to the method. we call it 'self'


three pillars of object oriented programming

1. encapsulation
keeping attributes isolated -- making sure object contains integral data

2. inheritance
creating classes that inherits values/attributes from other classes
class dog inherits from class animal
class Animal(object):
    def init
    def eat
class Dog(Animal)
    def fetch

dog = Dog()
dog.eat() # would work

3. polymorphism
same-named methods in two different cases can share a conceptual similarity


"""

class MyInt():
    def __init__(self):
        self.this_int = 0
    def increment(self):
        self.this_int = self.this_int + 1
    def get(self):
        return self.this_int

class Car(object):
    def __init__(self,arg1,arg2,arg3,arg4):
        self.drivetrain = arg1
        self.make = arg2
        self.model = arg3
        self.fueltype = arg4

mycar = Car('FWD','Honda','Civic','Gas')

print mycar.drivetrain
print mycar.make

x = MyInt()
print x.get()
x.increment()
x.increment()
print x.get()

exit()

class Obj():
    def something(self):
        print 'ok'

x = Obj()
x.something()

exit()

class Name(object):
    def setname(self, name):
        self.thisname = name

myname = Name()
print myname             # $ <__main__.Name object at 0x105ec4890>
myname.setname('jess')
print myname.thisname    # $ jess


exit()
class MyClass(object):
    def hello(self):
        print 'hey there'


myobj = MyClass()

myobj.x = 5
myobj.y = 10
myobj.z = 'test'

print myobj
print myobj.x
print myobj.y
print myobj.z
print myobj.__dict__
print myobj.hello()