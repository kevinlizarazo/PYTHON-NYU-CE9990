#!/usr/bin/env python
"""kevin_lizarazo_2-1.py -- count from 0-100 by user factor"""

step_counter = 0
position = 0

while True:
	user_input_string = raw_input('please enter an integer: ')
	if user_input_string.isdigit() :
		step_counter = int(user_input_string)
		print 'thank you. loading... '
		break
	else:
		print 'not an integer. try again'

print "counting from 0 to 100 by {}".format(user_input_string)

while position <= 100:
	print position
	position = position + step_counter
	