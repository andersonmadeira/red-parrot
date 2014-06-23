#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import array
import operator
from collections import Counter

def get_list_from_dict(sorted_dict):
    """Translates the sorted dict into a sorted list of nodes"""
    # map 
    return map(lambda (symbol,freq): HuffmanNode(symbol, freq), sorted_dict)

class HuffmanNode:
    def __init__(self, symbol=None, freq=None, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

    def __cmp__(self, other): # create a cmp function so nodes may be compared to each other with > < == 
        if self.freq < other.freq:
            return -1
        elif self.fre == other.freq:
            return 0
        else:
            return 1

    def __str__(self):
        return str(self.symbol) + '->' + str(self.freq)

def get_freq_from(filename, chunk_size=1):
    if chunk_size == 1:
        f = open(filename, 'rb') # input file
        a = array.array('B') # creates an array of bytes
        a.fromstring(f.read()) # feeds array with contents of 'filename'
        c = Counter(a) # counts the occurrences of each byte in the given file
        c_ord = sorted(c.iteritems(), key=operator.itemgetter(1))
        l = get_list_from_dict(c_ord)
            
        print 'Counted dict:',c
        print 'Sorted dict:', c_ord
        print 'List:'
        for e in l:
            print str(e),
        print
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
