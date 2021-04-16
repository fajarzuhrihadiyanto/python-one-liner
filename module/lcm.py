"""
lcm Lambda Function

Description :
    This lambda function is used to get least common multiple
    of the given list of integer

Example :
    input :
        [56, 24, 18]
    output :
        504
"""

from functools import reduce

lcm = lambda array_of_number: min([x for x in range(max(array_of_number), reduce(lambda a, b: a * b, array_of_number)) if all([x % y == 0 for y in array_of_number])])
