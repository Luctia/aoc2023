import numpy as np

from Day import Day


def shove_rocks(platform: [str], direction) -> [str]:
    # We will always shove the loose rocks all the way to the right. In order to make sure this gives the right result,
    #  we will have to rotate the platform.
    if direction == "N":
        npa = np.array([list(row) for row in platform])
        npa = np.rot90(npa, 3)
        platform = [''.join(row) for row in npa]
    if direction == "W":
        npa = np.array([list(row) for row in platform])
        npa = np.rot90(npa, 2)
        platform = [''.join(row) for row in npa]
    if direction == "S":
        npa = np.array([list(row) for row in platform])
        npa = np.rot90(npa, 1)
        platform = [''.join(row) for row in npa]

    new_platform = []
    for row in platform:
        col = 0
        loose_rocks = 0
        loose_rock_groups = []
        while col < len(row):
            if row[col] == 'O':
                loose_rocks += 1
            if row[col] == '#':
                loose_rock_groups.append(loose_rocks)
                loose_rocks = 0
            col += 1
        loose_rock_groups.append(loose_rocks)
        new_row = ['#' if c == '#' else '.' for c in row[::-1]]

        col = 0
        added = 0
        while col < len(new_row):
            if new_row[col] == '#':
                loose_rock_groups.pop()
                added = 0
            elif loose_rock_groups[-1] > added:
                added += 1
                new_row[col] = 'O'
            col += 1
        new_platform.append(new_row[::-1])

    if direction == "N":
        npa = np.array([list(row) for row in new_platform])
        npa = np.rot90(npa, 1)
        return [''.join(row) for row in npa]
    if direction == "W":
        npa = np.array([list(row) for row in new_platform])
        npa = np.rot90(npa, 2)
        return [''.join(row) for row in npa]
    if direction == "S":
        npa = np.array([list(row) for row in new_platform])
        npa = np.rot90(npa, 3)
        return [''.join(row) for row in npa]
    return new_platform


class Day14(Day):
    def part1(self, test=False):
        platform = self.get_input_lines('test' if test else '')
        shoved_north = shove_rocks(platform, "N")
        total = 0
        for i, line in enumerate(shoved_north):
            total += len(list(filter(lambda x: x == 'O', line))) * (len(shoved_north) - i)
        return total

    def part2(self, test=False):
        platform = self.get_input_lines('test' if test else '')
        for i in range(181):
            platform = shove_rocks(platform, 'N')
            platform = shove_rocks(platform, 'W')
            platform = shove_rocks(platform, 'S')
            platform = shove_rocks(platform, 'E')
        total = 0
        for i, line in enumerate(platform):
            total += len(list(filter(lambda x: x == 'O', line))) * (len(platform) - i)
        return total
