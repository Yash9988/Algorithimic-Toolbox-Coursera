# python3

from collections import namedtuple
from sys import stdin
from statistics import mode

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):

    points = []
    while len(segments) != 0:
        end_points = [i.end for i in segments]
        min_point = min(end_points)
        points.append(min_point)
        i = 0
        while i != (len(segments)):
            if segments[i].start <= min_point <= segments[i].end:
                segments.remove(segments[i])
                i -= 1
            i += 1

    return points

if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
