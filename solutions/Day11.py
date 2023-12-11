from Day import Day
import numpy as np


def get_expanded_chart(chart_rows):
    i = 0
    while i < len(chart_rows):
        if all([c == '.' for c in chart_rows[i]]):
            chart_rows = chart_rows[:i] + [chart_rows[i]] + chart_rows[i:]
            i += 2
        else:
            i += 1
    i = 0
    while i < len(chart_rows[0]):
        if all([row[i] == '.' for row in chart_rows]):
            chart_rows = [row[:i] + '.' + row[i:] for row in chart_rows]
            i += 2
        else:
            i += 1
    return chart_rows


def get_manhattan(c1, c2):
    return np.abs(c1[0] - c2[0]) + np.abs(c1[1] - c2[1])


def get_expansion_points(chart_rows):
    res = ([], [])
    for i in range(len(chart_rows)):
        if all([c == '.' for c in chart_rows[i]]):
            res[0].append(i)
    for i in range(len(chart_rows[0])):
        if all([row[i] == '.' for row in chart_rows]):
            res[1].append(i)
    return res


def get_expanded_manhattan(c1, c2, expansion_points, expansion_factor=1000000):
    no_of_expansions = 0
    for row in range(c1[0] if c1[0] < c2[0] else c2[0], c2[0] if c1[0] > c2[0] else c1[0]):
        if row in expansion_points[0]:
            no_of_expansions += 1
    for col in range(c1[1] if c1[1] < c2[1] else c2[1], c2[1] if c1[1] < c2[1] else c1[1]):
        if col in expansion_points[1]:
            no_of_expansions += 1
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + no_of_expansions * (expansion_factor - 1)


class Day11(Day):
    def part1(self, test=False):
        chart_rows = self.get_input_lines("test" if test else "")
        chart_rows = get_expanded_chart(chart_rows)
        galaxies = []
        for y in range(len(chart_rows)):
            for x in range(len(chart_rows[y])):
                if chart_rows[y][x] == '#':
                    galaxies.append((y, x))
        distances = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                distances += get_manhattan(galaxies[i], galaxies[j])
        return distances

    def part2(self, test=False):
        chart_rows = self.get_input_lines("test" if test else "")
        expansion_points = get_expansion_points(chart_rows)
        galaxies = []
        for y in range(len(chart_rows)):
            for x in range(len(chart_rows[y])):
                if chart_rows[y][x] == '#':
                    galaxies.append((y, x))
        distances = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                distances += get_expanded_manhattan(galaxies[i], galaxies[j], expansion_points, 1 if test else None)
        return distances
