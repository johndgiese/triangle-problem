#!/usr/bin/python
import sys


def load_triangle_data(data_file):
    return [[int(n) for n in line.strip().split(" ")] for line in data_file]


class TriangleSolver(object):
    def __init__(self, triangle_data):
        self.data = triangle_data
        self.memoized_results = {}

    def max_path(self, r, c):
        key = (r, c)
        if key in self.memoized_results:
            return self.memoized_results[key]

        value = self.data[r][c]
        if r == 0:
            max_path = value
        elif c == 0:
            max_path = value + self.max_path(r - 1, 0)
        elif c == r:
            max_path = value + self.max_path(r - 1, c - 1)
        else:
            max_path = value + max(self.max_path(r - 1, c - 1), self.max_path(r - 1, c))

        self.memoized_results[key] = max_path
        return max_path

    def solve(self):
        height = len(self.data)
        return max([self.max_path(height - 1, c) for c in xrange(height)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: triangle.py datafile.txt")
        sys.exit(0)
    else:
        data_filename = sys.argv[1]

    with open(data_filename, 'r') as data_file:
        triangle_data = load_triangle_data(data_file)

    print(TriangleSolver(triangle_data).solve())
