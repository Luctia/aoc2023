from Day import Day
from sys import maxsize


def get_map(input_lines, type):
    i = 0
    while input_lines[i] != type:
        i += 1
    i += 1
    mapped = []
    while input_lines[i] != "":
        line = input_lines[i].split(" ")
        mapped.append((int(line[0]), int(line[1]), int(line[2])))
        i += 1
    mapped.sort(key=lambda x: x[1])
    return mapped


def lookup_in_map(value, mapped):
    if value is None:
        return None
    for tup in mapped:
        if tup[1] <= value < tup[1] + tup[2]:
            return tup[0] + value - tup[1]
    return value


def get_seed_location(seed, input_lines):
    seed_soil = get_map(input_lines, "seed-to-soil map:")
    soil_fert = get_map(input_lines, "soil-to-fertilizer map:")
    fert_wat = get_map(input_lines, "fertilizer-to-water map:")
    wat_light = get_map(input_lines, "water-to-light map:")
    light_temp = get_map(input_lines, "light-to-temperature map:")
    temp_hum = get_map(input_lines, "temperature-to-humidity map:")
    hum_loc = get_map(input_lines, "humidity-to-location map:")
    return lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(seed, seed_soil), soil_fert), fert_wat), wat_light), light_temp), temp_hum), hum_loc)


def get_maps(input_lines):
    return [
        get_map(input_lines, "seed-to-soil map:"),
        get_map(input_lines, "soil-to-fertilizer map:"),
        get_map(input_lines, "fertilizer-to-water map:"),
        get_map(input_lines, "water-to-light map:"),
        get_map(input_lines, "light-to-temperature map:"),
        get_map(input_lines, "temperature-to-humidity map:"),
        get_map(input_lines, "humidity-to-location map:")
    ]


def get_new_ranges(ranges, m):
    new_ranges = []
    for start, end in ranges:
        i = 0
        while start < end:
            dest, source, rng = m[i]
            i += 1
            if start < source:
                # Beginning of range falls off
                new_ranges.append((start, source - 1))
                start = source
            if start < source + rng:
                # Some part of the range is in this mapping
                new_entry = (dest + start - source, dest + end - source if end < source + rng else dest + rng)
                new_ranges.append(new_entry)
                start = source + rng
            if i >= len(m) and start < end:
                # We've reached the end of the map. Put leftovers back as literals
                new_ranges.append((start, end))
                break
    return sorted(new_ranges)


class Day05(Day):
    def part1(self):
        input_lines = self.get_input_lines()
        seeds = [int(seed) for seed in input_lines[0].split(" ")[1:]]
        lowest_loc = maxsize
        for seed in seeds:
            location = get_seed_location(seed, input_lines)
            if location is not None and location < lowest_loc:
                lowest_loc = location
        self.answer(lowest_loc)

    def part2(self):
        input_lines = self.get_input_lines()
        maps = get_maps(input_lines)
        seeds = [int(seed) for seed in input_lines[0].split(" ")[1:]]
        seed_ranges = []
        for i in range(0, len(seeds) - 1, 2):
            seed_ranges.append((seeds[i], seeds[i] + seeds[i+1] - 1))
        ranges = sorted(seed_ranges)
        for m in maps:
            ranges = get_new_ranges(ranges, m)
        self.answer(min(ranges)[0])
