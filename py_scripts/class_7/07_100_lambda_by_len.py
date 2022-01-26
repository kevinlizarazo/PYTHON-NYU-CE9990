#!/usr/bin/env python
"""
def by_len(this_string):
    return len(this_string)

mystrs = ['abcdefg', 'abc', 'ab', 'a', 'abcdefghij']

smystrs = sorted(mystrs, key=by_len)
"""


def by_len(this_string):
    return len(this_string)

mystrs = ['abcdefg', 'abc', 'ab', 'a', 'abcdefghij']

smystrs = sorted(mystrs, key=lambda this_string: len(this_string))