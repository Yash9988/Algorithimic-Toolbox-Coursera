# python3
import numpy as np
import operator

opr = []
m = M = np.array([])


def findmm(i, j):
    min1 = 1000
    max1 = -1000
    for k in range(i, j):
        if opr[k - 1] == "+":
            a = operator.add(M[i, k], M[k + 1, j])
            b = operator.add(m[i, k], M[k + 1, j])
            c = operator.add(M[i, k], m[k + 1, j])
            d = operator.add(m[i, k], m[k + 1, j])
        elif opr[k - 1] == "-":
            a = operator.sub(M[i, k], M[k + 1, j])
            b = operator.sub(m[i, k], M[k + 1, j])
            c = operator.sub(M[i, k], m[k + 1, j])
            d = operator.sub(m[i, k], m[k + 1, j])
        elif opr[k - 1] == "*":
            a = operator.mul(M[i, k], M[k + 1, j])
            b = operator.mul(m[i, k], M[k + 1, j])
            c = operator.mul(M[i, k], m[k + 1, j])
            d = operator.mul(m[i, k], m[k + 1, j])
        else:
            a = operator.truediv(M[i, k], M[k + 1, j])
            b = operator.truediv(m[i, k], M[k + 1, j])
            c = operator.truediv(M[i, k], m[k + 1, j])
            d = operator.truediv(m[i, k], m[k + 1, j])

        min1 = min(min1, a, b, c, d)
        max1 = max(max1, a, b, c, d)

    return int(min1), int(max1)


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    var = list(dataset)
    global opr, m, M
    opr = var[1::2]
    d = var[::2]
    n = len(d)
    m = np.zeros((n+1, n+1))
    M = np.zeros((n+1, n+1))
    for i in range(1, n + 1):
        m[i, i] = d[i - 1]
        M[i, i] = d[i - 1]

    for s in range(1, n + 1):
        for i in range(1, n - s + 1):
            j = i + s
            m[i, j], M[i, j] = findmm(i, j)

    return int(M[1, n])


if __name__ == "__main__":
    print(find_maximum_value(input()))
