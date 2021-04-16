"""
pyramid Lambda Function

Description :
    This lambda function is used to get string representation
    of pyramid pattern with given height of the pyramid

Example :
    input :
        5
    output :
            *
           ***
          *****
         *******
        *********
"""

pyramid = lambda height: '\n'.join([(i * '*').center(2 * height - 1) for i in range(1, 2 * height, 2)])
