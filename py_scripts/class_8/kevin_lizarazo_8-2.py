#!/usr/bin/env python

""" watched directory """

import sys
import os
import time

working_set = set()
sys.argv

try:
    path = sys.argv[1]
    files = os.listdir(path)
except IndexError:
    exit('please enter one argument')
except OSError:
    exit('no such directory')

for file in files:
    working_set.add(file)

while True:
    files = os.listdir(path)
    time.sleep(5)
    current_set = set()
    for file in files:
        current_set.add(file)
    deletions = working_set.difference(current_set)
    additions = current_set.difference(working_set)
    for file in deletions:
        print "{} deleted".format(file)
    for file in additions:
        print "{} added".format(file)
    working_set = current_set

