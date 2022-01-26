#!/usr/bin/env python

uin = raw_input('please enter a number: ')
unum = float(uin)

if unum > 0 and unum % 2 == 0:
	print 'number is greater than 0, and is even'
elif unum > 0:
	print 'number is greater than 0'
elif unum < 0:
	print 'number is less than 0'
else:
	print 'number is 0'
