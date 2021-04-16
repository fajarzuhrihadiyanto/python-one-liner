"""
rectangle Lambda Function

Description :
    This lambda function is used to get string representation
    of triangle pattern with given height of the triangle

Example :
    input :
        5
    output :
        *
        **
        ***
        ****
        *****
"""

triangle = lambda height: '\n'.join([i * '*' for i in range(1, height+1)])
