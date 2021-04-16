"""
Factor Lambda Function

Description :
    This Lambda function is used to get
    list of factor pair of the given number

Example :
    input :
        20
    output :
         [(1, 20), (2, 10), (4, 5)]
"""

import math

factor = lambda number: [(x, number // x) for x in range(1, int(math.sqrt(number) + 1)) if number % x == 0]
