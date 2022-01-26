#!/usr/bin/env python

"""
# writes to the STDOUT (standard out) data stream
# by default: the screen
# STDOUT can be redirected at the command line through
# > redirection operator. "python notes.py > out.txt"
# the >> operator appends output to file.
# the > operator truncates/wipes and writes output to file.

ls shows dir
ls / shows parent dir
pwd displays current working directory
wc shows lines/word/chars count
grep -l <term> * shows files that have search them in it

you can use them in combination.
ls > filelist.txt creates a text file with the ls results.

pipe " | " 
notes.py | wc 
output from script into input of command
notes.py | wc shows the line/word/char count for the script output 
"hello world"  ## 1    2    12

wc | notes.py
- directs command into script


< operator directs the text of a file to the STD (standard in) 
of a script.
wc < out.txt
- directs file into script, to be manipulated by script just like
a file handler

                            hello.py->wc
notes.py | wc        # pipe STDOUT->STDIN (from one script to the other)
notes.py > out.txt   # write STDOUT to file
notes.py < in.txt    # read file to STDIN
notes.py arg1 arg2   # pass string args to program

"""
"""
# script that takes two args and adds them together as ints

import sys

sys.argv

arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

print arg1 + arg2

# $ python notes.py 10 15
# 25
"""
"""
# listing files and dirs in directories
# reading file metadata (file size, etc)

import os

#files = os.listdir('.') # '.' = just get present working directory
path = '../python_data/bible'
files = os.listdir(path)

for line in files:
    filepath = os.path.join(path, line)
    this_file_size = os.path.getsize(filepath)
    print "{}: {} bytes".format(line, this_file_size)
    for verse in open(filepath):
        verse = verse.rstrip()
        print "{}: {}".format(line, verse)

"""

# add these two command line args as integers, print result
# trapping exceptions

import sys

try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
except IndexError:
    exit('please enter two args')

try:
    intarg1 = int(arg1)
    intarg2 = int(arg2)
except ValueError:
    exit('args must be ints')

print intarg1 + intarg2
