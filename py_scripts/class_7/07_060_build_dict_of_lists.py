#!/usr/bin/env python

filename = '../../python_data/student_db.txt'

fh = open(filename)

for line in fh:
    student_id, street, city, state, zip = line.split(':')
    print student_id
