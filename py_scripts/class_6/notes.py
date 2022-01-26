#!/usr/bin/env python
"""
def pborder(length):
    print '=' * length

def add(v1, v2):
    total = v1 + v2
    print total
    return total


thissum = add('hello','world')

print thissum + ' return value'
"""

""" many programs begin with a group of functions.

functions() don't return values. they are blocs of code to run functions you
would use within the rest of the code. when a function is called, Python
looks for it and executes the bloc.

if an arg or args is passed in the call, they are copied to the names
in the function def. if the # ofargs don't match = error. Python doesn't 
care about type, it just attempts it anyway

if you want to return the value, use the 'return' keyword. it can be 
assigned to a new variable in the call.
without a return value, python returns None

variables inside the function are scoped TO the function. i.e. cannot
print variable from within function, outside the function.

def functions() = no args
def functions(arg) = one arg
def functions(arg, arg2) = two args

SORTING BELOW'

SORTING

strings sort alphabetically

# mydict.get() function can return value if passed key argument
# key=mydict.get is not a function call
# if we were to type key=len, the keys would be sorted by their own length
# "key=" tells Python to call the function with each key.
# whatever comes back from that function is the value by which each key
# should be sorted

1. if we pass a dict to sorted, sorted() will sort the keys.
2. if we note a func in key=, Python will call that func once
    for each key in the dict. again: there can only be one key.
    but it is called as many times as there are elements in the dict
    (or now a list, since sorted() returns a list)
3. whatever is returned from that call, is the value by which
    that key should be sorted. 

mydict = {'a': 100, 'b': 10, 'c': 500}

sdict = sorted(mydict, key=mydict.get)
print sdict

"""
"""

1. py identifies the things to be sorted (a list of strings below)
2. py checks to see if there is a key= arg
3. if there is, it calls the function for each item in the sortable list
4. whatver is returned from the func is the val by which that item should be sorted

def bynum(arg):
    value = int(arg)
    return value

mylist = ['1', '103', '11', '1002']
slist = sorted(mylist, key=bynum)
print slist

def bylast(arg):
    argument = arg.split()
    return argument[1]

names = ['David Blaikie', 'Joe Wilson', 'Pete Abercrombie', 'Paula Zimmerman']
snames = sorted(names, key=bylast)
print snames

var = [[1,2,3], ['a','b','c'], [0.1,0.2,0.3]]

BACK TO MULTIDIMENSIONAL STRUCTURES BELOW

for x in var:
    #print x[-1]
    for y in x:
        print y
"""

var = {'a': [1,2,3],
     'b': [100,200,330]}

total = 0

for x in var:
    y = var[x]
    sumil = sum(y)
    print sumil

