#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import array
from collections import Counter

def get_file_content(filename):
    f = open(filename, 'rb') # input file
    a = array.array('B') # creates an array of bytes
    a.fromstring(f.read()) # feeds array with contents of 'filename'
    print Counter(a) # counts the occurrencies of each byte in the given file
    

def main(filename):
    get_file_content(filename)
    pass

def show_usage():
    print 'Usage:', os.path.basename(sys.argv[0]), '<inputfile>'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        show_usage()
