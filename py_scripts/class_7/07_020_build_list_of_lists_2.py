#!/usr/bin/env python

import pprint

filename = '../../python_data/small_db.txt'

fh = open(filename)

list1 = []

for line in fh:
    line = line.rstrip()
    id, name, revenue = line.split(':')
    list1.append([id, name, float(revenue)])

pprint.pprint(list1)
