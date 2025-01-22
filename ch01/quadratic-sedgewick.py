#!/usr/bin/python3

#
#   File:
#      quadratic-sedgewick.py
#
#   Synopsis:
#
#
#   Revision History:
#       Date             Change Description
#      ------ -----------------------------------------
#      250120 Original.
#
#
#   a == 1?!?

import math
import sys
import stdio

b = float(sys.argv[1])
c = float(sys.argv[2])

discriminant = b * b - 4.0 * c
d = math.sqrt(discriminant)

stdio.writeln((-b + d) / 2.0)
stdio.writeln((-b - d) / 2.0)

