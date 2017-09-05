def rotate(matrix):
    row_len = len(matrix)
    for diagonal in range(row_len//2):

        for row_start in range(diagonal, row_len - diagonal - 1):
            start_i, start_j = diagonal, row_start
            next_val = matrix[start_i][start_j]

            for edge in range(4):
                next_i, next_j = abs(row_len - start_j - 1), start_i
                temp = matrix[next_i][next_j]
                matrix[next_i][next_j] = next_val
                next_val = temp
                start_i, start_j = next_i, next_j
    return matrix
