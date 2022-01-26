#!/usr/bin/env python

while True:
    user_input = raw_input('please enter a filename: ')
    if user_input == 'sawyer.txt':
        fh = open('../../../python_data/sawyer.txt')
        break
    else:
        print 'this computer suggests you type "sawyer.txt" without quotes'

text = fh.read()
char_count = len(text)

text_lines = text.splitlines()
line_count = len(text_lines)

text_words = text.split()
word_count = len(text_words)


print str(line_count).rjust(8), str(word_count).rjust(8), str(char_count).rjust(8), user_input.rjust(8)