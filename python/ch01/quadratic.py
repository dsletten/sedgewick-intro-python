#!/usr/bin/python3

#
#   File:
#      quadratic.py
#
#   Synopsis:
#
#
#   Revision History:
#       Date             Change Description
#      ------ -----------------------------------------
#      250120 Original.
#

import math
import sys
import stdio

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

discriminant = b * b - 4.0 * a * c
d = math.sqrt(discriminant)

# Goldberg -- What Every Computer Scientist Should Know... pg. 162
if b >= 0:
    stdio.writeln((2 * c) / (-b - d))
    stdio.writeln((-b - d) / (2.0 * a))
else:
    stdio.writeln((-b + d) / (2.0 * a))
    stdio.writeln((2 * c) / (-b + d))

# stdio.writeln((-b + d) / (2.0 * a))
# stdio.writeln((-b - d) / (2.0 * a))

