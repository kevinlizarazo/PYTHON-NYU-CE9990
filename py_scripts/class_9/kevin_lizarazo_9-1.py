#!/usr/bin/env python

"""modules file"""

def getlines(filename, newlines=False):
    fh = open(filename)
    if newlines is True:
        processed_lines = fh.read().splitlines()
        fh.close()
        return processed_lines
    processed_lines = fh.readlines()
    fh.close()
    return processed_lines

def gettext(filename):
    fh = open(filename)
    text = fh.read()
    fh.close()
    return text

def getfields(filename, delimiter=None):
    fields = []
    fh = open(filename).readlines()
    for line in fh:
        if not delimiter:
            line = line.rstrip().split()
        else:
            if delimiter is not (':'):
                raise ValueError ('bad delimiter')
            line = line.rstrip().split(delimiter)
        fields.append(line)
    fh.close()
    return fields
