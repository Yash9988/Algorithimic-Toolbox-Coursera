# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n
    if n >= 10 ** 10:
        a = [0] * int(n/10**9)
    elif n >= 10 ** 5:
        a = [0] * int(n/10 ** 3)
    else:
        a = [0] * (n * 100)
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

    sum1 = 0
    mo = mo[:-1]
    l = int(n / len(mo))
    if l > 0:
        sum1 += sum(mo) * l
    sum1 += sum(mo[:(n%len(mo)+1)])

    return sum1%10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
