# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    change = 0
    curr = 0
    if money >= 10:
        remain = money % 10
        curr += (money - remain) / 10
        money -= curr * 10
    change += curr
    curr = 0

    # print(money, change)

    if money >= 5:
        remain = money % 5
        curr += (money - remain) / 5
        money -= curr * 5
    change += curr
    curr = 0

    # print(money, change)

    if money >= 1:
        remain = money % 1
        curr += money - remain
        money -= curr
    change += curr

    # print(money, change)

    return int(change)


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
