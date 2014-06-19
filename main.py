#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import array
import operator
from collections import Counter

def get_freq_from(filename, chunk_size=1):
    if chunk_size == 1:
        f = open(filename, 'rb') # input file
        a = array.array('B') # creates an array of bytes
        a.fromstring(f.read()) # feeds array with contents of 'filename'
        c = Counter(a) # counts the occurrencies of each byte in the given file
        c_ord = sorted(c.iteritems(), key=operator.itemgetter(1))
        print c
        print c_ord
        print 'Most freq.:', c_ord[len(c_ord)-1] # shows the most frequent byte
        print 'Least freq.:', c_ord[0] # shows the least frequent byte
    else: # @TODO: compression using blocks of bytes as words for higer compression ratio com bigger files.
        pass

def main(filename):
    get_freq_from(filename)
    pass

def show_usage():
    print 'Usage:', os.path.basename(sys.argv[0]), '<inputfile>'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        show_usage()
