#!/usr/bin/env python

import pprint

filename = '../../python_data/small_db.txt'

fh = open(filename)

odict = {}

for line in fh:
    line = line.rstrip()
    cid, name, revenue = line.split(':')
    revenue = float(revenue)
    odict[cid] = {'name': name, 'revenue': revenue}

pprint.pprint(odict)
    
