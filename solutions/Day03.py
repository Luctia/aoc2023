import re

from Day import Day


def build_adjacent_tiles(location):
    return [
        (location[0] - 1, location[1]),
        (location[0] + 1, location[1]),
        (location[0], location[1] - 1),
        (location[0], location[1] + 1),
        (location[0] - 1, location[1] - 1),
        (location[0] + 1, location[1] - 1),
        (location[0] - 1, location[1] + 1),
        (location[0] + 1, location[1] + 1)
    ]


def get_adjacent_tiles(location, lines):
    adjacent_coordinates = build_adjacent_tiles(location)
    adjacent_tiles = set()
    for coordinate in adjacent_coordinates:
        if 0 <= coordinate[0] < len(lines[0]) and 0 <= coordinate[1] < len(lines):
            adjacent_tiles.add(lines[coordinate[1]][coordinate[0]])
    return adjacent_tiles


def is_relevant_part_number(location, match, lines, pattern=r'\d|\.|\n'):
    coordinates = [(x, location[1]) for x in [*range(match.start(), match.end())]]
    for coordinate in coordinates:
        adjacent_tiles = get_adjacent_tiles(coordinate, lines)
        for tile in adjacent_tiles:
            if not re.match(pattern, tile):
                return True
    return False


def has_intersection(star_co, match_location, match):
    star_adjacent_coordinates = build_adjacent_tiles(star_co)
    for i in range(len(match.group())):
        loc = (match_location[0] + i, match_location[1])
        if loc in star_adjacent_coordinates:
            return True
    return False


class Day03(Day):

    def part1(self):
        y = 0
        matches = dict()
        lines = self.get_input_lines()
        for line in lines:
            for match in re.finditer(r'\d+', line):
                matches[(match.start(), y)] = match
            y += 1
        relevantPartNumbers = []
        for match in matches:
            if is_relevant_part_number(match, matches[match], lines):
                relevantPartNumbers.append(int(matches[match].group()))
        self.answer(sum(relevantPartNumbers))

    def part2(self):
        y = 0
        matches = dict()
        lines = self.get_input_lines()
        stars = []
        val = 0
        for line in lines:
            for match in re.finditer(r'\d+', line):
                matches[(match.start(), y)] = match
            for match in re.finditer(r'\*', line):
                stars.append((match.start(), y))
            y += 1
        for star in stars:
            intersecting = []
            for match in matches:
                if has_intersection(star, match, matches[match]):
                    intersecting.append(matches[match])
            if len(intersecting) == 2:
                val += int(intersecting[0].group()) * int(intersecting[1].group())
        self.answer(val)
