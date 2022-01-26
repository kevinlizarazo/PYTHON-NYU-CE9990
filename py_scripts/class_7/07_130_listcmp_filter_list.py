#!/usr/bin/env python


# filter
"""
y = [ -20, -15, -10, -5, 0, 5, 10, 15, 20 ]

x = [ 1, 2, 3, 11, 12, 13, 101, 102, 103 ]
"""

x = ['id1:this', 'id2:that']

ids = []
for item in x:
    myid = item.split(':')[0]
    ids.append(myid)

ids = [ item.split(':')[0] for item in x ]