#!/usr/bin/python3

#
#   File:
#      random-range.py
#
#   Synopsis:
#
#
#   Revision History:
#       Date             Change Description
#      ------ -----------------------------------------
#      250214 Original.
#
#
#    Ex. 1.2.16

import random
import sys
import stdio

def random_range(a, b):
    if a > b:
        return random_range(b, a)
    else:
        r = random.Random()
        r.seed()

        # https://docs.python.org/3/library/random.html#random.randint
        return r.randint(a, b)

a = int(sys.argv[1])
b = int(sys.argv[2])

stdio.writeln("Random [" + str(a) + "," + str(b) + "]: " + str(random_range(a, b)))
