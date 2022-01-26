#!/usr/bin/env python

"""
ymd = '20150503'

mon = ymd[4:6]

yr = ymd[0:4]

print mon
print yr

# string slice rules
# string slices return a new string
# lower bound is zero inclusive
# upper bound is non-inclusive (one above desired end)

"""


"""
second_column_sum = 0.0

fh = open('../py_data/FF_abbreviated.txt')

for line in fh:
    line = line.rstrip()
    els = line.split()
    second_column_sum = second_column_sum + float(els[1])
    print 'line els', els

print 'sum of the second column is {}'.format(second_column_sum)

"""




"""
loop through a file line by line
each line is a string
split the string whether on delimiter or whitespace
split returns a list


"""




"""
var = 'this     is     a     string'

var2 = var.split() # removes all whitespace

print repr(var)
print repr(var2)
"""



"""

# rstrip() strips off right side
# lstrip() strips off left side
# strip() strips off both sides
# repr() prints full representation of the string

"""

"""

# the split() method
# takes a string delimiter argument
# returns a list of strings based on the source string
# separated on delimiter
# it also removes all whitespace

var = 'this:that:there'

split_var = var.split(':')

print split_var 
print len(split_var)
"""

"""
fh = open('../py_data/students.txt')
xx = fh.readlines()
print xx
print 'lines: ', len(xx)

fh = open('../py_data/students.txt')
xx = fh.read()
print xx
print 'characters: ', len(xx)


# read() returns one big string. 
# readlines() returns a 'list' of strings.

"""

"""
xx = open('../py_data/students.txt')


counter = 0
for yy in xx:      # 'for' loops once for every line in the file
    print yy       # yy is assigned each line (a string)
    counter = counter + 1

print; print 'done. there were {} lines'.format(counter)
"""