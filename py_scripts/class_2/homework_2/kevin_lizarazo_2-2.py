#!/usr/bin/env python
"""kevin_lizarazo_2-2.py -- count from 1-user value, sum up along the way"""

end_value = 0
total = 0
counter = 0

while True:
    user_input_string = raw_input('please enter an integer: ')
    if user_input_string.isdigit():
        end_value = int(user_input_string)
        print 'thank you. loading... '
        break
    else:
        print 'not an integer. try again'

while counter <= end_value:
    total = total + counter
    counter = counter + 1

print "sum from 1 to {} is {}".format(end_value, total)