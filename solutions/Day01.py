import re
from sys import maxsize

from Day import Day


STRING_NUM_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def find(needle, haystack):
    try:
        return haystack.index(needle), needle
    except ValueError:
        return maxsize, None


def find_reverse(needle, haystack):
    try:
        indices = [m.start() for m in re.finditer(needle, haystack)]
        return max(indices), needle
    except ValueError:
        return -1, None


class Day01(Day):
    def part1(self):
        sum = 0
        for line in self.get_input_lines():
            digits = re.findall('\d', line)
            sum += int(digits[0] + digits[-1])
        Day.answer(sum)

    def part2(self):
        sum = 0
        for line in self.get_input_lines():
            firstkey = min(find(word, line) for word in STRING_NUM_MAPPING)
            secondkey = max(find_reverse(word, line) for word in STRING_NUM_MAPPING)
            firstdigit = STRING_NUM_MAPPING[firstkey[1]]
            lastdigit = STRING_NUM_MAPPING[secondkey[1]]
            result = int(firstdigit + lastdigit)
            sum += int(result)
        Day.answer(sum)
