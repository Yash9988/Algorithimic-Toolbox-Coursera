# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    indv = []
    for i in range(len(weights)):
        indv.append(prices[i] / weights[i])

    total = 0
    profit = 0
    while total < capacity:
        if max(indv) == 0:
            break
        precious = indv.index(max(indv))
        if weights[precious] + total <= capacity:
            profit += prices[precious]
            total += weights[precious]
            indv[precious] = 0
        else:
            profit += ((capacity - total) / weights[precious]) * prices[precious]
            total = capacity
            indv[precious] = 0

    return profit


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
