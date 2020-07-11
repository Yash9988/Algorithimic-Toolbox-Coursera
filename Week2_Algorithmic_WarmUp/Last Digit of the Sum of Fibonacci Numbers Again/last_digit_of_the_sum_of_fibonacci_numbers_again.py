# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    m = from_index
    n = to_index
    if n <= 1:
        return n
    if n >= 10 ** 8:
        a = [0] * int(n / 10 ** 6)
    else:
        a = [0] * (n * 100)
    a[0] = 0
    a[1] = 1
    mo = [0, 1]
    i = 2
    while True:
        a[i] = a[i - 1] + a[i - 2]
        if a[i - 1] % 10 == a[0] and a[i] % 10 == a[1]:
            break
        mo.append(a[i] % 10)
        i += 1

    sum1 = 0
    mo = mo[:-1]
    l = int((n - m)/ len(mo))
    sum1 += sum(mo) * l
    if m < len(mo):
        sum1 += sum(mo[m:])
    else:
        sum1 += sum(mo[m % len(mo):])
    sum1 += sum(mo[:n % len(mo) + 1])

    return sum1 % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
