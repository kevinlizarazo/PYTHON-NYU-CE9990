#!/usr/bin/env python
"""
var = 0

while var < 5:
    print var
    var = var + 1

print 'done'
"""

var = 5
total = 0
total_even = 0
total_odd = 0

while var >= 0:
    print var
    total = total + var
    if var % 2 == 0:
        total_even = total_even + var
    else:
        total_odd = total_odd + var
    var = var - 1

print 'total of the even numbers: ', total_even
print 'total of the odd numbers: ', total_odd
print 'total: ', total




