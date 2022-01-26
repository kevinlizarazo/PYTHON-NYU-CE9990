#!/usr/bin/env python 
""" dictionaries and sorting """

""" dicts pair unique keys with associated values 

i.e. students with GPA
companies with revenues

some things we can do with sequences:
add, len, loop, slice, subscript, sort

# refresher:
mylist = [1,2,'a','b'] #ordered mutable
mytuple = (1,4,'b','zzzz') #ordered immutable 
myset = set([1,4,4.3,5.3,6.5]) #unordered unique collection
#
"""
"""
print 'dictionary'
mydict = {'a': 20, 'b': 5, 'c': 10} # a, c, b
print mydict

print 'returning dictionary with key and value'
for x in mydict:
    key_value = '{} {}'.format(x, mydict[x])
    print key_value

print 'sorted dictionary'
skeys = sorted(mydict) # returns sorted keys
print skeys

print 'returning dict sorted by key'
for x in skeys:   # x is a key 
    key_value = '{} {}'.format(x, mydict[x])
    print key_value
    
print 'return of mydict.items()'
dis = mydict.items()
print dis

print 'returning targeted elements of mydict.items()'
for x in mydict.items():
    print x[0],',', x[1]

# print mydict['a']
# ^ ^ ^ how to subscript. it doesnt take an index, it takes the key


    """
""""
MULTI TARGETING VARIABLES.
THERE MUST BE EXACTLY AS MANY VARIABLES 
AS THERE ARE COLUMNS IN FILE

ff = '../py_data/FF_abbreviated.txt'
fh = open(ff)

for line in fh:
    ymd, mktrf, hml, smb, rf = line.split()
"""
"""================================="""
### ADDING KEY AND VALUE INTO AN EMPTY DICT
"""
mydict = {}

fh = open('../py_data/student_db.txt')
lines = fh.readlines()[1:]

for line in lines:
    line = line.rstrip() # process the line to remove newline char
    sid, street, city, state, zipcode = line.split(':')
    mydict[sid] = [street, city, state, zipcode]

print mydict['ak9']

"""

"""
mydict = {  'a': [1, 2, 3], 
            'b': [4, 5, 6], 
            'c': [7, 8, 9]
         }

print (mydict['b'])[-1]   # 6

xx = mydict['b']
print xx[-1]              # 6

"""
"""
mydict = {}

mydict['key1'] = 10
mydict['key1'] = mydict['key1'] * 2
print mydict

fh = open('../py_data/F-F_Research_Data_Factors_daily.txt')
reader = fh.readlines()
fh.close()
"""

#### COUNTING DICTIONARY

statedict = {}
fh = open('../py_data/student_db.txt')

for line in fh.readlines()[1:]:
    stuid, street, city, state, zipc = line.split(':')
    if state not in statedict:
        statedict[state] = 1
    else:
        statedict[state] = statedict[state] + 1

print statedict

print 'sorted values'

sorted_keys = sorted(statedict, key=statedict.get)
print sorted_keys




