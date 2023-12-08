from Day import Day


class Day08(Day):
    def part1(self, test=False):
        lines = self.get_input_lines()
        instructions = lines[0]
        mappings = dict()
        for mapping in lines[2:]:
            mappings[mapping[0:3]] = (mapping[7:10], mapping[12:15])
        i = 0
        location = "AAA"
        while location != "ZZZ":
            location = mappings[location][0 if instructions[i % len(instructions)] == "L" else 1]
            i += 1
        return i

    def part2(self, test=False):
        lines = self.get_input_lines()
        instructions = lines[0]
        mappings = dict()
        for mapping in lines[2:]:
            mappings[mapping[0:3]] = (mapping[7:10], mapping[12:15])
        i = 0
        locations = [key for key in mappings.keys() if key[-1] == "A"]
        while not all([location[-1] == "Z" for location in locations]):
            for j in range(len(locations)):
                locations[j] = mappings[locations[j]][0 if instructions[i % len(instructions)] == "L" else 1]
            i += 1
        return i
