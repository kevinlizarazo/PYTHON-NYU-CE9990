#!/usr/bin/env python

import pprint

filename = '../../python_data/small_db.txt'

fh = open(filename)

outer_dict = {}


for line in fh:
    line = line.rstrip()
    id, name, revenue = line.split(':')
    revenue = float(revenue)
    outer_dict[id] = [name,revenue]

pprint.pprint(outer_dict)

