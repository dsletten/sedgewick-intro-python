#!/usr/bin/python3

#
#   File:
#      usethree.py
#
#   Synopsis:
#
#
#   Revision History:
#       Date             Change Description
#      ------ -----------------------------------------
#      241217 Original.
#

import sys
import stdio

stdio.writeln("Hi " + sys.argv[3] + ", " + sys.argv[2] + ", and " + sys.argv[1] + ".")
sys.argv[1] = "and " + sys.argv[1]
stdio.writeln("Hi " + ", ".join(sys.argv[1:][::-1]) + ".")
