# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    i = 1
    sum1 = 0
    while sum1 <= n:
        if sum1 == n:
            break
        sum1 += i
        summands.append(i)
        i += 1

    l = sum(summands)
    if l > n:
        for i in summands:
            if l - i == n:
                summands.remove(i)

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
