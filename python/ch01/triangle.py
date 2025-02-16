#!/usr/bin/python3

#
#   File:
#      triangle.py
#
#   Synopsis:
#
#
#   Revision History:
#       Date             Change Description
#      ------ -----------------------------------------
#      250204 Original.
#
#    Ex. 1.2.12
#    
#    https://en.wikipedia.org/wiki/Triangle_inequality
#
#    Explicitly: a + b > c  &  b + c > a  &  a + c > b
#    Equivalently: |a - b| < c < a + b
#    or
#    max(a, b, c) < a + b + c - max(a, b, c) => 2 max(a, b, c) < a + b + c
#    or
#    Area of triangle > 0.
#    

import math
import sys
import stdio

def is_triangle_sedgewick(a, b, c):
    return not (a >= (b + c) or b >=(a + c) or c >= (a + b))

def is_triangle(a, b, c):
    return a < (b + c) and b < (a + c) and c < (a + b)

def is_triangle_abs(a, b, c):
    return abs(a - b) < c and c < a + b

def is_triangle_max(a, b, c):
    return 2 * max(a, b, c) < a + b + c

#
#    Assumes a ≥ b ≥ c
#
def heron(sides):
    [a, b, c] = sides
    product = (a + (b + c)) * (c - (a - b)) * (c + (a - b)) * (a + (b - c))

    if product < 0:
        return 0
    else:
        return math.sqrt(product) / 4

def goldberg_heron(a, b, c):
    return heron(sorted([a, b, c], reverse = True))

def is_triangle_area(a, b, c):
    return goldberg_heron(a, b, c) > 0

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if is_triangle_sedgewick(a, b, c):
    stdio.writeln(True)
else:
    stdio.writeln(False)

if is_triangle(a, b, c):
    stdio.writeln(True)
else:
    stdio.writeln(False)

if is_triangle_abs(a, b, c):
    stdio.writeln(True)
else:
    stdio.writeln(False)

if is_triangle_max(a, b, c):
    stdio.writeln(True)
else:
    stdio.writeln(False)

if is_triangle_area(a, b, c):
    stdio.writeln(True)
else:
    stdio.writeln(False)
    
    
