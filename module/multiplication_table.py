"""
multiplication_table Lambda Function

Description :
    This lambda function is used to get string representation
    of multiplication table with the given row and col

Example :
    input :
        5, 5
    output :
        1 * 1 = 1     2 * 1 =  2     3 * 1 =  3     4 * 1 =  4     5 * 1 =  5
        1 * 2 = 2     2 * 2 =  4     3 * 2 =  6     4 * 2 =  8     5 * 2 = 10
        1 * 3 = 3     2 * 3 =  6     3 * 3 =  9     4 * 3 = 12     5 * 3 = 15
        1 * 4 = 4     2 * 4 =  8     3 * 4 = 12     4 * 4 = 16     5 * 4 = 20
        1 * 5 = 5     2 * 5 = 10     3 * 5 = 15     4 * 5 = 20     5 * 5 = 25
"""

multiplication_table = lambda row, col: '\n'.join(["     ".join([(str(x).rjust(max(len(str(row)), len(str(col)))) + " * " + str(y).rjust(max(len(str(row)), len(str(col)))) + " = " + str(x * y).rjust(len(str(x * row)))) for x in range(1, col + 1)]) for y in range(1, row + 1)])
