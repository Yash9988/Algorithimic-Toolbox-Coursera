# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    coins = [0] * (money + 1)
    for i in range(1, money + 1):
        if i - 1 >= 0 and i - 3 >= 0 and i - 4 >= 0:
            coins[i] = min(coins[i - 1], coins[i - 3], coins[i - 4]) + 1
        elif i - 1 >= 0 and i - 3 >= 0:
            coins[i] = min(coins[i - 1], coins[i - 3]) + 1
        else:
            coins[i] = coins[i - 1] + 1
    return coins[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
