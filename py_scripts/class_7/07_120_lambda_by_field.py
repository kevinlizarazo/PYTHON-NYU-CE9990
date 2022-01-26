#!/usr/bin/env python

def by_third(line):
   items = line.split(',')
   floatval = float(items[2])
   return floatval

filename = '../../python_data/small_db.txt'

fh = open(filename)

lines = fh.readlines()

slines = sorted(lines, key=by_third)

for line in slines:
    print line
