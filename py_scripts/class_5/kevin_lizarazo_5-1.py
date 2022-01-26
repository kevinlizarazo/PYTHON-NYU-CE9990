#!/usr/bin/env python
# Student dictionary processor

students = {}

fh = open('../py_data/student_db.txt')
students_db = fh.readlines()[1:]

for student in students_db:
    student = student.rstrip()
    student_id, address, city, state, zipcode = student.split(':')
    student_id = student_id.lower()
    students[student_id] = [address, city, state, zipcode]

print "{} records loaded.".format(len(students))
print "all student IDs have been lowercased."

while True:
    user_input = raw_input('please enter a student ID or press "q" to quit: ')
    if user_input == 'q':
        exit()
    if user_input in students:
        address, city, state, zipcode = students[user_input]
        print "address for {}:\n{}\n{}, {} {}".format(user_input, address, city, state, zipcode)
        continue 
    else:
        print 'error. try again'

