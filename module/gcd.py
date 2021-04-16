"""
gcd Lambda Function

Description :
    This lambda function is used to get greatest common divisor
    of the given list of integer

Example :
    input :
        [24, 36, 48]
    output :
         12
"""

gcd = lambda array_of_number: max([x for x in range(1, min(array_of_number) + 1) if all([y % x == 0 for y in array_of_number])])