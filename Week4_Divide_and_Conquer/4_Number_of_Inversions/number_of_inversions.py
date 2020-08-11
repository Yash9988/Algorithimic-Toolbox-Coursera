# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    def inv_rec(a):
        if len(a) == 1:
            return [0, a]
        mid = len(a) // 2
        left = inv_rec(a[:mid])
        right = inv_rec(a[mid:])
        return merge(left, right)

    def merge(left, right):
        count_inv = left[0] + right[0]
        left_arr = left[1]
        right_arr = right[1]

        result = []
        while len(left_arr) > 0 and len(right_arr) > 0:
            if left_arr[0] > right_arr[0]:
                result.append(left_arr[0])
                count_inv += len(right_arr)
                del(left_arr[0])

            else:
                result.append(right_arr[0])
                del(right_arr[0])

        result = result + left_arr
        result = result + right_arr

        return [count_inv, result]

    return inv_rec(a)[0]


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
