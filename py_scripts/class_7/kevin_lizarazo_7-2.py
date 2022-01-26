#!/usr/bin/env python

""" list comp with students db """

print [ el.split(':')[0] for el in open('../python_data/student_db.txt').readlines()[1:] ]