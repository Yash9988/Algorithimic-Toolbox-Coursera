# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    ops = [0] * (n + 1)
    seq = []
    for i in range(2, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            ops[i] = min(ops[i - 1], ops[i // 2], ops[i // 3]) + 1
        elif i % 2 == 0:
            ops[i] = min(ops[i - 1], ops[i // 2]) + 1
        elif i % 3 == 0:
            ops[i] = min(ops[i - 1], ops[i // 3]) + 1
        else:
            ops[i] = ops[i - 1] + 1

    i = n
    while i != 1 and i != 0:
        seq.append(i)
        if i % 2 == 0 and i % 3 == 0:
            x = (i - 1, ops[i - 1])
            y = (i // 2, ops[i // 2])
            z = (i // 3, ops[i // 3])
            m = min(x[1], y[1], z[1])
            if m == z[1]:
                i = z[0]
            if m == y[1]:
                i = y[0]
            if m == x[1]:
                i = x[0]
        elif i % 2 == 0:
            x = (i - 1, ops[i - 1])
            y = (i // 2, ops[i // 2])
            m = min(x[1], y[1])
            if m == y[1]:
                i = y[0]
            if m == x[1]:
                i = x[0]
        elif i % 3 == 0:
            x = (i - 1, ops[i - 1])
            y = (i // 3, ops[i // 3])
            m = min(x[1], y[1])
            if m == y[1]:
                i = y[0]
            if m == x[1]:
                i = x[0]
        else:
            x = (i - 1, ops[i - 1])
            i = x[0]
    seq.append(1)

    return list(reversed(seq))


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
