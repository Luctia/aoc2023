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
    return mapped


def lookup_in_map(value, mapped):
    if value is None:
        return None
    for tup in mapped:
        if tup[1] <= value < tup[1] + tup[2]:
            return tup[0] + value - tup[1]
    return None


def get_seed_location(seed, input_lines):
    seed_soil = get_map(input_lines, "seed-to-soil map:")
    soil_fert = get_map(input_lines, "soil-to-fertilizer map:")
    fert_wat = get_map(input_lines, "fertilizer-to-water map:")
    wat_light = get_map(input_lines, "water-to-light map:")
    light_temp = get_map(input_lines, "light-to-temperature map:")
    temp_hum = get_map(input_lines, "temperature-to-humidity map:")
    hum_loc = get_map(input_lines, "humidity-to-location map:")
    return lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(lookup_in_map(seed, seed_soil), soil_fert), fert_wat), wat_light), light_temp), temp_hum), hum_loc)


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
        seeds = [int(seed) for seed in input_lines[0].split(" ")[1:]]
        seed_ranges = []
        for i in range(len(seeds) - 1):
            seed_ranges.append((seeds[i], seeds[i] + seeds[i+1] - 1))

        # lowest_range = None
        # lowest_found = maxsize
        #
        # for r in seed_ranges:
        #     for num in range(r[0], r[1], (r[1] - r[0]) // 10):
        #         loc = get_seed_location(num, input_lines)
        #         if loc is not None and loc < lowest_found:
        #             lowest_found = loc
        #             lowest_range = r

        lowest_range = None
        lowest_found = maxsize
        i = 0
        for r in seed_ranges:
            i += 1
            print("Considering range " + str(i))
            print("  (lowest so far: " + str(lowest_found) + ")")
            picks = [num for num in range(r[0], r[1] + 4, (r[1] - r[0]) // 4)]
            for pick in range(0, len(picks) - 1):
                print("    pick " + str(pick + 1) + " of 4")
                rrange = (picks[pick], picks[pick + 1])

                if get_seed_location(rrange[0], input_lines) is None:
                    pass
                if get_seed_location(rrange[1], input_lines) is None:
                    while get_seed_location(rrange[1], input_lines) is None:
                        rrange = rrange[0], rrange[1] - 100

                diff = rrange[1] - rrange[0]
                while diff > 1:
                    left_guess_seed = rrange[0] + diff // 4
                    right_guess_seed = rrange[0] + (diff // 4) * 3
                    left_guess_location = get_seed_location(left_guess_seed, input_lines)
                    while left_guess_location is None:
                        left_guess_seed = left_guess_seed + 10000
                        left_guess_location = get_seed_location(left_guess_seed, input_lines)
                    right_guess_location = get_seed_location(right_guess_seed, input_lines)
                    while right_guess_location is None:
                        right_guess_seed = right_guess_seed - 10000
                        right_guess_location = get_seed_location(right_guess_seed, input_lines)
                    if left_guess_location < right_guess_location:
                        rrange = rrange[0], rrange[0] + diff // 2
                    else:
                        rrange = rrange[0] + diff // 2, rrange[1]
                    diff = rrange[1] - rrange[0]
                lowest_found = min([lowest_found, left_guess_location, right_guess_location])

        self.answer(lowest_found)
