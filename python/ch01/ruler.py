#!/usr/bin/python3

#
#   File:
#      ruler.py
#
#   Synopsis:
#
#
#   Revision History:
#       Date             Change Description
#      ------ -----------------------------------------
#      250109 Original.
#

import stdio

# ruler1 = '-\n'
# ruler2 = ruler1 + '--\n' + ruler1
# ruler3 = ruler2 + '---\n' + ruler2
# ruler4 = ruler3 + '----\n' + ruler3

ruler1 = '—\n'
ruler2 = ruler1 + '——\n' + ruler1
ruler3 = ruler2 + '———\n' + ruler2
ruler4 = ruler3 + '————\n' + ruler3

stdio.writeln(ruler1)
stdio.writeln(ruler2)
stdio.writeln(ruler3)
stdio.writeln(ruler4)

