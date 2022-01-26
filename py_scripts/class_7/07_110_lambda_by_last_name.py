#!/usr/bin/env python

def by_last_name(name):
    items = name.split()
    return items[2]

names = ['Joe Wilson', 'Zeb Apple', 'Jim Beatty']

snames = sorted(names, key=by_last_name)
