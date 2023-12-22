import re
from itertools import permutations

from Day import Day


def is_arranged_correctly(line: str, configuration: list[int]) -> bool:
    groups = re.findall(r'#+', line)
    if len(groups) != len(configuration):
        return False
    for i in range(len(configuration)):
        if len(groups[i]) != configuration[i]:
            return False
    return True


def try_configurations(line: str) -> int:
    defects, config = line.split(" ")
    config = [int(x) for x in config.split(',')]
    q = defects.count('?')
    total = sum(config) - defects.count('#')
    perms = permutations((['#'] * total) + (['.'] * (q - total)), q)
    correct_defects = []
    for perm in perms:
        j = 0
        adjusted_defects = defects
        for i in range(len(defects)):
            if defects[i] == '?':
                adjusted_defects = adjusted_defects[:i] + perm[j] + adjusted_defects[(i + 1):]
                j += 1
        if is_arranged_correctly(adjusted_defects, config) and adjusted_defects not in correct_defects:
            correct_defects.append(adjusted_defects)
    return len(correct_defects)


class Day12(Day):
    def part1(self, test=False):
        return sum([try_configurations(line) for line in self.get_input_lines()])

    def part2(self, test=False):
        pass
