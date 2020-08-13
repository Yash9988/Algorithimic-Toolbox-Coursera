# python3

from itertools import product
from sys import stdin
import numpy as np


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    if sum(values) % 3 != 0 or max(values) > sum(values) // 3:
        return 0

    mat = np.zeros((sum(values) // 3 + 1, len(values) + 1))

    for i in range(1, sum(values) // 3 + 1):
        for j in range(1, len(values) + 1):
            ii = i - values[j - 1]
            if values[j - 1] == i or (ii > 0 and mat[ii, j - 1]):
                mat[i, j] = 1 if mat[i, j - 1] == 0 else 2
            else:
                mat[i, j] = mat[i, j - 1]

    return 1 if mat[sum(values) // 3, len(values)] else 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
