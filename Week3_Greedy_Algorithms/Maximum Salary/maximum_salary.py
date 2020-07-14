# python3

from itertools import permutations


def largest_number_naive(numbers):
    print(numbers)
    numbers = list(map(str, numbers))
    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int(''.join(permutation)))

    return largest


def largest_number(numbers):
    res = ""
    number = numbers
    while len(number) > 0:
        max_ = number[0]
        for i in number:
            max_ = i if str(max_) + str(i) < str(i) + str(max_) else max_
        res += str(max_)
        number.remove(max_)

    return res


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
