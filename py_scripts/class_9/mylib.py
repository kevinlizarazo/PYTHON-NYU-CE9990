#!/usr/bin/env python

def doubleit(arg):
    doublearg = arg * 2
    return doublearg

def getcol(filename, colindex):
    fh = open('../python_data/' + filename)
    mylist = []
    for line in fh:
        fields = line.split()
        field = fields[colindex]
        mylist.append(field)
    return mylist



"""
def doubleit(yy, mult=2): #positional arguments must be there. x
                    #parameter/keyword arguments come with defaults. mult=2
    doublearg = yy * mult
    return doublearg

x = doubleit(2,mult=3)


doublearg, yy, mult, are LOCAL vars 
they are local because they were created in the function

x is a GLOBAL variable
because it was created outside a function

len, str, list, open, sorted
are examples of BUILTIN vars

"""