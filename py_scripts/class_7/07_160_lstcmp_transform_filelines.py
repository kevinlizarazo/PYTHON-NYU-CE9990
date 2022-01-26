#!/usr/bin/env python

fh = open('Fama-French_data.txt')

mktrf_vals = []

for line in fh:
    line = line.rstrip()
    items = line.split()
    mktrf = items[2]
    mktrf = float(mktrf)
    wanted_lines.append(line)


print mktrf_vals
