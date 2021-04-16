"""
is_prime Lambda Function

Description :
    This lambda function is used to check if
    the given number is prime or not

Example :
    input :
        21
    output :
        False
"""

is_prime = lambda number: False if number == 1 else (True if number == 2 else not any([number % x == 0 for x in range(2, number)]))
