#!/usr/bin/env python

x = set([1, 2, 3, 4])
y = set([3, 4, 5, 6])

common = x.intersection(y)
difference = x.difference(y)
union = x.union(y)

print common
print difference
print union