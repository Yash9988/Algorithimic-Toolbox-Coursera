# python3
import numpy as np


def edit_distance(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    mat = np.zeros((m + 1, n + 1))

    for i in range(m + 1):
        mat[i, 0] = i

    for i in range(n + 1):
        mat[0, i] = i

    for j in range(1, n+1):
        for i in range(1, m+1):
            if first_string[i - 1] == second_string[j - 1]:
                mat[i, j] = min(mat[i, j - 1] + 1, mat[i - 1, j] + 1, mat[i - 1, j - 1])
            else:
                mat[i, j] = min(mat[i, j - 1] + 1, mat[i - 1, j] + 1, mat[i - 1, j - 1] + 1)

    return int(mat[m, n])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
