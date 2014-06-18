#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

def main(filename):
    pass

def show_usage():
    print 'Usage:', os.path.basename(sys.argv[0]), '<inputfile>'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        show_usage()
