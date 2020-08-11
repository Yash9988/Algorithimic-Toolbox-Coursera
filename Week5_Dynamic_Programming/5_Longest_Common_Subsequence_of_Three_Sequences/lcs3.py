# python3
import numpy as np

def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    m = len(first_sequence)
    n = len(second_sequence)
    o = len(third_sequence)

    mat = np.zeros((m + 1, n + 1, o + 1))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if first_sequence[i - 1] == second_sequence[j - 1] and first_sequence[i - 1] == third_sequence[k - 1]:
                    mat[i, j, k] = mat[i - 1, j - 1, k - 1] + 1
                else:
                    mat[i, j, k] = max(max(mat[i - 1, j, k], mat[i, j - 1, k]), mat[i, j, k - 1])

    return mat[i, j, k]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
