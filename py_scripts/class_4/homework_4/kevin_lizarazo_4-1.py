#!/usr/bin/env python 
"""Calculate through F-F data file according to user year input and user factor input"""

dataset = []
factors = ['MKT-RF', 'SMB', 'HML', 'RF']
factor_selector = 0
fh = open('../py_data/F-F_Research_Data_Factors_daily.txt')
reader = fh.readlines()
fh.close()

while True:
    user_input = raw_input('please enter a four digit year: ')
    if user_input.isdigit() and len(user_input) == 4:
        print 'available factors: {}'.format(factors)
        user_factor = raw_input('please enter a factor: ')
        user_factor = user_factor.upper()
        if user_factor == factors[0]:
            factor_selector = 1
            break
        elif user_factor == factors[1]:
            factor_selector = 2
            break
        elif user_factor == factors[2]:
            factor_selector = 3
            break
        elif user_factor == factors[3]:
            factor_selector = 4
            break
        else:
            print 'not an available factor. restarting'
    else:
        print 'not a four year input. try again'

for line in reader[5:-2]:
    year = line[0:4]
    if user_input == year:
        elements = line.split()
        data = float(elements[factor_selector])
        dataset.append(data)

if not dataset:
    print 'no year data found'
    exit()

count = len(dataset)
data_sum = sum(dataset)
data_avg = data_sum / count
data_max = max(dataset)
data_min = min(dataset)
data_sorted = sorted(dataset)
data_med = data_sorted[len(data_sorted) / 2]

print '{} ({}): {} values, max {}, min {}, avg {}, median {}'.format(user_input, user_factor, count, data_max, data_min, data_avg, data_med)




