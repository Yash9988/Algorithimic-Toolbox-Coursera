# python3

from random import randint


def partition3(array, left, right):
    x = array[left]
    begin = left + 1
    end = left

    for i in range(left + 1, right + 1):
        if array[i] <= x:
            end += 1
            array[i], array[end] = array[end], array[i]
            if array[end] < x:
                array[begin], array[end] = array[end], array[begin]
                begin += 1

    array[left], array[begin - 1] = array[begin - 1], array[left]

    return [begin, end]


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    [m1, m2] = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
