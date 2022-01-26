#!/usr/bin/env python

fh = open('Fama-French_data.txt')

wanted_lines = []

for line in fh:
    if line.startswith('1928'):
        wanted_lines.append(line)



for line in wanted_lines:
    print line
