#!/usr/bin/python3

#
#   File:
#      divides.py
#
#   Synopsis:
#
#
#   Revision History:
#       Date             Change Description
#      ------ -----------------------------------------
#      250202 Original.
#

import math
import sys
import stdio

m = int(sys.argv[1])
n = int(sys.argv[2])

if m > 0 and n > 0:
    stdio.writeln(m % n == 0 or n % m == 0)
else:
    stdio.writeln("Corrupt")

    
