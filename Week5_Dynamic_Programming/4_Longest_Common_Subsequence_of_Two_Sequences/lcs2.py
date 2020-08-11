# python3
import numpy as np

def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    m = len(first_sequence)
    n = len(second_sequence)

    mat = np.zeros((m+1, n+1))
    for i in range(m + 1):
        mat[i, 0] = 0
    for j in range(n + 1):
        mat[0, j] = 0

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                mat[i, j] = mat[i - 1, j - 1] + 1
            else:
                mat[i, j] = max(mat[i - 1, j], mat[i, j - 1])

    return int(mat[m, n])


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
