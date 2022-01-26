#!/usr/bin/env python

"""
def bylen(this_string):
    return len(this_string)

mystrs = ['this', 'a', 'about', 'alphabet']
smystrs = sorted(mystrs, key=bylen)

print smystrs
"""
"""
def byval(this_key_val):
    return mydict[this_key_val]

mydict = {'a': 5, 'b': 100, 'c': 0.5}
smydict_keys = sorted(mydict, key=byval)

print smydict_keys
"""

def bysum(arg):
    return sum(mydict[arg])

mydict = {
   'z':  [1, 3, 5, 9, 7, 1, 0.3],
   'a':  [100, 150, 139],
   'm':  [15, 45]
}

smydict = sorted(mydict, key=lambda arg: sum(mydict[arg]))
print smydict