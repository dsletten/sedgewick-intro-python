#!/usr/bin/python3

#
#   File:
#      intops.py
#
#   Synopsis:
#
#
#   Revision History:
#       Date             Change Description
#      ------ -----------------------------------------
#      250115 Original.
#

import sys
import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])

total = a + b
difference = a - b
product = a * b
quotient = a // b
modulo = a % b
power = a ** b

stdio.writeln(str(a) + ' +  ' + str(b) + ' = ' + str(total))
stdio.writeln(str(a) + ' -  ' + str(b) + ' = ' + str(difference))
stdio.writeln(str(a) + ' *  ' + str(b) + ' = ' + str(product))
stdio.writeln(str(a) + ' // ' + str(b) + ' = ' + str(quotient))
stdio.writeln(str(a) + ' %  ' + str(b) + ' = ' + str(modulo))
stdio.writeln(str(a) + ' ** ' + str(b) + ' = ' + str(power))
