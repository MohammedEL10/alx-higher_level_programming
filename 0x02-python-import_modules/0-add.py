#!/usr/bin/python3
"""print the some 1 and 2"""
from add_0 import add
a = 1
b = 2
if (__name__ == '__main__'):
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
