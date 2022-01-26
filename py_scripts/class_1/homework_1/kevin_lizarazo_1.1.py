#!/usr/bin/env python

var_1 = int(raw_input('Please enter an integer: '))
var_2 = int(raw_input('Please enter another integer: '))
var_3 = var_1 ** var_2
var_4 = len(str(var_3))

print '=' * var_4
print var_3
print '=' * var_4

# I started out with a variable for each operation.
# I figured that simplifying/combining the functions
# could make the code more readable. But with Python,
# is that considered "best practice?"
