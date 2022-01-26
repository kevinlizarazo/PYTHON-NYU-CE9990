#!/usr/bin/env python

"""modules script"""

import filelib

data_file = '../python_data/student_db.txt'

lines = filelib.getlines(data_file, newlines=True)
print len(lines)

text = filelib.gettext(data_file) 
print len(text)

list_of_lists = filelib.getfields(data_file, delimiter=':') 
print list_of_lists