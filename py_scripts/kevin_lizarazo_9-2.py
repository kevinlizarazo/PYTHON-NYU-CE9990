#!/usr/bin/env python

"""working with classes"""

class Square():
    def __init__(self):
        self.this_int = 2
    def squareme(self):
        self.this_int = self.this_int * self.this_int
    def getme(self):
        return self.this_int

n1 = Square()
n2 = Square()
n3 = Square()

n1.squareme()
val1 = n1.getme()
print val1

n2.squareme()
n2.squareme()
val2 = n2.getme()
print val2
print n1.getme()

n3.squareme()
n3.squareme()
n3.squareme()
n3.squareme()
n3.squareme()
val3 = n3.getme()
print val3

print n1.getme()
print n2.getme()
print n3.getme()