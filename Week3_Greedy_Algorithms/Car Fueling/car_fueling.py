# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    if m >= d:
        return 0

    count = 0
    current = 0
    while (current+m) < d:
        x = 0

        if (current + m) in stops:
            current = current + m
            count += 1
            x = 1
        else:
            for i in range(current + m, current, -1):
                if i in stops:
                    current = i
                    count += 1
                    x = 1
                    break

        if x == 0:
            count = -1
            return count

    return count



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
