# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n
    if n > 10 ** 10:
        a = [0] * int(n/10 ** 8)
    elif n > 10 ** 4:
        a = [0] * int(n/10 ** 2)
    else:
        a = [0] * (n * 10**3)
    a[0] = 0
    a[1] = 1
    mo = [0, 1]
    i = 2
    while True:
        a[i] = a[i - 1] + a[i - 2]
        if a[i - 1] % m == a[0] and a[i] % m == a[1]:
            break
        mo.append(a[i] % m)
        i += 1

    mo = mo[:-1]
    l = len(mo)
    return mo[n % l]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
