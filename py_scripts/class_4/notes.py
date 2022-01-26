#!/usr/bin/env python 

# take input, validate it, transform it, then report
# ETL = extract, transform, load


# LIST

""" 
list is an ordered, mutable sequence of objects

# things we can do with a list: 
    len, sum, min, max, subscript, slice, 
    loop through with for, append, sort, test for membership
# slice of string returns chars. 
# slice of list returns elements

mylist = []
mylist.append(3)
mylist.append(2)

mymax = max(mylist)
mymin = min(mylist)
mysum = sum(mylist)
mylen = float(len(mylist))
sortlist = sorted(mylist)
avg = mysum / mylen

for el in mylist:
    do something;

if 3 in mylist:
    do something;

print mylist

print "min {} sum {} len {} max {} avg {}".format(mymin,mysum,mylen,mymax,avg)

"""

# TUPLE 

"""
tuple is an ordered, immutable sequence of objects

WORKS: len, sum, subscript, slice (which slices elements not chars),
       testing for membership, sort (but this returns a list)

DOES NOT WORK: append (tuple object has no attribute/method 'append')

tuples are IMMUTABLE. they cannot be appended. 
tuple object does not support item assignment.

benefits to immutability: memory management 

x = (4, 5, 6, 6.4, 2.8)
"""

# SET 

"""
unordered, mutable, UNIQUE collection of objects

WORKS: len, sum min max, sort (but this returns list),
        for loops (but returns out of order), test membership, add

add(): adds an element, but if it already exists, 
       it does not add a duplicate

DOESN'T WORK: subscript (sets don't support indexing), slice

myset = {1, 5.6, 99, 2, 3}

myset.add(3)
myset.add(100)

for el in myset:
    print el

"""


















