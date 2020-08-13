# python3
import numpy as np
from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    mat = np.zeros((capacity + 1, len(weights) + 1))

    for j in range(1, len(weights) + 1):
        for i in range(1, capacity + 1):
            mat[i, j] = mat[i, j - 1]
            if weights[j - 1] <= i:
                val = mat[i - weights[j - 1], j - 1] + weights[j - 1]
                if mat[i, j] < val:
                    mat[i, j] = val

    return int(mat[capacity, len(weights)])




if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
