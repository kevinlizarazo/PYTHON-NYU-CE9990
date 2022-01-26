#!/usr/bin/env python

while True:
    user_input = raw_input('please enter a four digit year: ')
    if user_input.isdigit() and len(user_input) == 4:
        print 'thank you. loading... '
        break
    else:
        print 'not a four year input. try again'

mrkt_ref_sum = 0.0
count = 0 

fh = open ('../py_data/Fama-French_data.txt')

for line in fh:
    year = line[0:4]
    if user_input == year:
        elements = line.split()
        mrkt_ref_sum = mrkt_ref_sum + float(elements[1])
        count = count + 1

average = mrkt_ref_sum / count

print "{} data was found {} times. Market ref total is {}. The average market ref is {}".format(user_input, count, mrkt_ref_sum, average)
        