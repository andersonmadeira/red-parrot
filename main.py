#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import array
import bisect
import operator
from collections import Counter

def print_tree(root):
    # draw a tree like this
##    root
##      +--sub1
##      +--sub2
##      |  +--sub2sub1
##      +--sub3
##         +--sub3sub1
##         |  +--sub3sub1sub1
##         +--sub3sub2
    pass
    

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
        elif self.freq == other.freq:
            return 0
        else:
            return 1

    def __str__(self):
        return str(self.symbol) + '->' + str(self.freq)
        

def get_tree_freq_from(filename, chunk_size=1):
    if chunk_size == 1:
        f = open(filename, 'rb') # input file
        a = bytearray(f.read()) # creates an array of bytes with contents of 'filename'
        c = Counter(a) # counts the occurrences of each byte in the given file
        c_ord = sorted(c.iteritems(), key=operator.itemgetter(1))
        L = get_list_from_dict(c_ord) # list of node objects that will remain sorted during the algorithm

        for e in L:
            print e,
        print

        n = len(L)
        for i in xrange(n-1):
            new_node = HuffmanNode('*') # non-terminal node.
            new_node.left = L.pop(0) # take the the two with the lowest frequency
            new_node.right = L.pop(0)
            new_node.freq = new_node.left.freq + new_node.right.freq
            bisect.insort_left(L, new_node) # append the new node in the right place so the list will remain sorted.
        return L.pop(0) # returns the root of the huffman tree
        
        #print 'Most freq.:', c_ord[len(c_ord)-1] # shows the most frequent byte
        #print 'Least freq.:', c_ord[0] # shows the least frequent byte
    else: # @TODO: compression using blocks of bytes as words for higer compression ratio com bigger files.
        pass

def main(filename):
    print_tree(get_tree_freq_from(filename))
    pass

def show_usage():
    print 'Usage:', os.path.basename(sys.argv[0]), '<inputfile>'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        show_usage()
