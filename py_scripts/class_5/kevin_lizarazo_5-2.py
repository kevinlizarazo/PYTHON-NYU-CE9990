#!/usr/bin/env python
""" F-F Research Data sums and sorters of year-blocs """

data = dict()
fh = open('../py_data/F-F_Research_Data_Factors_daily.txt')
daily_returns = fh.readlines()[5:-2]

for line in daily_returns:
    line = line.split()
    year = line[0][0:4]
    mkt_rf = float(line[1])
    if year not in data:
        data[year] = 0.0
    data[year] = data[year] + mkt_rf

data_length = len(data)
        
while True:
    results_input = raw_input('enter the desired # of results displayed or "q" to quit: ')
    if results_input == 'q':
        exit()
    if not results_input.isdigit():
        print "error: input not an integer"
        continue
    results = int(results_input)
    if results > data_length:
        print "error: more desired results than data length"
        continue
    sort_dir_input = (raw_input('sort by "highest" or "lowest": ')).lower()
    if sort_dir_input not in ['highest','lowest']:
        print "error: input not 'highest' or 'lowest'"
        continue
    if sort_dir_input == "highest":
        reverse_arg = True
    if sort_dir_input == "lowest":
        reverse_arg = False
    break

sorted_data = sorted(data, reverse=reverse_arg, key=data.get)
for line in sorted_data[0:results]:
    print "{}: {}".format(line, data[line])