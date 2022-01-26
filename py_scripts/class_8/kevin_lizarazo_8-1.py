#!/usr/bin/env python

""" Directory grep """

import sys
import os

sys.argv

try:
    path = sys.argv[1]
    query = sys.argv[2]
    files = os.listdir(path)
except IndexError:
    exit('please enter two arguments')
except OSError:
    exit('no such directory')

for file in files:
    filepath = os.path.join(path, file)
    count = 0
    for line in open(filepath):
        count = count + 1
        line = line.rstrip()
        if query in line:
            print "{} ({}): {}".format(file, count, line)
        


