#!/usr/bin/env python 
"""Sawyer.txt spell checker"""

dictionary = set()
line_count = 1

fh = open('../py_data/words.txt')

for element in fh:
    element = element.rstrip()
    element = element.rstrip(":;,.")
    element = element.lower()
    dictionary.add(element)

fh.close()

fh = open('../py_data/sawyer.txt')
text = fh.read()
text = text.splitlines()

for line in text:
    line = line.split()
    for word in line:
        word = word.rstrip()
        word = word.rstrip(':;,.')
        word = word.lower()
        if word not in dictionary:
            print 'misspelled word on line {}: {}'.format(line_count, word)
    line_count = line_count + 1

fh.close()