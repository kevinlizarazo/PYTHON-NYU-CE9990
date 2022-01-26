#!/usr/bin/env python

subtotal = float(raw_input('Please enter the total bill amount: '))
guests = int(raw_input('Please enter the number in your party: '))
unconverted_tip = float(raw_input('Please enter desired tip percentage: '))
tip = subtotal * (unconverted_tip * .01)

total = subtotal + tip

split_total = total / guests



print 'A ' + str(unconverted_tip) + '% tip ' + '($' + str(tip) +') was added to the bill, for a total of $' + str(total)

print 'With ' + str(guests) + ' in your party, each person must pay $' + str(split_total)
