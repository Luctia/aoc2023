from Day import Day
from sys import maxsize


def get_map(input_lines, type):
    found = False
    i = 0
    while input_lines[i] != type:
        i += 1
    i += 1
    mapped = []
    while input_lines[i] != "":
        line = input_lines[i].split(" ")
        mapped.append((int(line[0]), int(line[1]), int(line[2])))
        i += 1
    return mapped


def lookup_in_map(value, mapped):
    if value is None:
        return None
    for tup in mapped:
        if tup[1] <= value < tup[1] + tup[2]:
            return tup[0] + value - tup[1]
    return None


class Day05(Day):
    def part1(self):
        input_lines = self.get_input_lines()
        seeds = [int(seed) for seed in input_lines[0].split(" ")[1:]]
        seed_soil = get_map(input_lines, "seed-to-soil map:")
        soil_fert = get_map(input_lines, "soil-to-fertilizer map:")
        fert_wat = get_map(input_lines, "fertilizer-to-water map:")
        wat_light = get_map(input_lines, "water-to-light map:")
        light_temp = get_map(input_lines, "light-to-temperature map:")
        temp_hum = get_map(input_lines, "temperature-to-humidity map:")
        hum_loc = get_map(input_lines, "humidity-to-location map:")
        lowest_loc = maxsize
        for seed in seeds:
            location = lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(seed, seed_soil), soil_fert), fert_wat), wat_light), light_temp), temp_hum), hum_loc)
            if location is not None and location < lowest_loc:
                lowest_loc = location
        self.answer(lowest_loc)

    def part2(self):
        input_lines = self.get_input_lines()
        seed_ranges = [int(seed) for seed in input_lines[0].split(" ")[1:]]
        seed_soil = get_map(input_lines, "seed-to-soil map:")
        soil_fert = get_map(input_lines, "soil-to-fertilizer map:")
        fert_wat = get_map(input_lines, "fertilizer-to-water map:")
        wat_light = get_map(input_lines, "water-to-light map:")
        light_temp = get_map(input_lines, "light-to-temperature map:")
        temp_hum = get_map(input_lines, "temperature-to-humidity map:")
        hum_loc = get_map(input_lines, "humidity-to-location map:")

        lowest_dest = maxsize
        lowest_range = None
        for x in hum_loc:
            if x[0] < lowest_dest:
                lowest_range = x
        start = lowest_range[1]
        end = start + lowest_range[2]

        lowest_ranges = []

        self.answer(1)
