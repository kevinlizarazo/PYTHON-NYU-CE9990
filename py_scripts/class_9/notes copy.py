#!/usr/bin/env python
"""
def doubleit(yy, mult=2): #positional arguments must be there. x
                    #parameter/keyword arguments come with defaults. mult=2
    doublearg = yy * mult
    return doublearg

x = doubleit(2,mult=3)
"""
""" 
doublearg, yy, mult, are LOCAL vars 
they are local because they were created in the function

x is a GLOBAL variable
because it was created outside a function

len, str, list, open, sorted
are examples of BUILTIN vars

"""
"""
a module is python code in a file.

all global variables in a module are accessible as attributes of the module name

doubleit is an attribute (also function). because we're accessing it from elsewhere,
doubleit is an attribute.

if there is a GLOBAL variable 'var = 10', and you wanted to print it in a script,
you would then write 'print mylib.var'

"""

import mylib

x = mylib.doubleit(500)

print x

"""
hw = write module in such a way that it raises an exception instead of exiting upon error

"""




