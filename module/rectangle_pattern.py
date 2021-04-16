"""
rectangle Lambda Function

Description :
    This lambda function is used to get string representation
    of rectangle pattern with given number of row and col of the rectangle

Example :
    input :
        3, 5
    output :
        *****
        *****
        *****
"""

rectangle = lambda row, col: row * (col * '*' + '\n')
