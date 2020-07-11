# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    if n >= 100000:
        a = [0] * int(n / 10**3)
    else:
        a = [0] * (n * 10**2)
    a[0] = 0
    a[1] = 1
    mo = [0, 1]
    i = 2
    m = 10
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
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
