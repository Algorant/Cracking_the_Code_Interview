'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
'''

def zero_mat_pythonic(matrix):
    matrix = [["X" if x == 0 else x for x in row] for row in matrix]
    indices = []

    for idx, row in enumerate(matrix):
        if "X" in row:
            indices = indices + [i for i, j in enumerate(row) if j == "X"]
            matrix[idx] = [0] * len(matrix[0])

    matrix = [[0 if row.index(i) in indices else i for i in row] for row in matrix]
    return matrix


m1 =[
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],

            ]

print(zero_mat(m1))
