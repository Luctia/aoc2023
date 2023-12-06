import re
import functools

from Day import Day


def get_win_options(mills, record):
    options = dict()
    for button_help_down_for in range(mills):
        distance = (mills - button_help_down_for) * button_help_down_for
        if distance > record:
            options[button_help_down_for] = distance
    return options


class Day06(Day):
    def part1(self, test=False):
        numbers = [int(n) for n in re.findall(r'\d+', self.get_input("test" if test else ""))]
        time_dist = dict()
        for i in range(len(numbers) // 2):
            time_dist[numbers[i]] = numbers[i + len(numbers) // 2]
        product = 1
        for key in time_dist:
            product *= len(get_win_options(key, time_dist[key]))
        return product

    def part2(self, test=False):
        numbers = re.findall(r'\d+', self.get_input("test" if test else ""))
        time_dist = dict()
        time_dist[int(functools.reduce(lambda x, y: x + y, numbers[:len(numbers) // 2], ""))] = int(functools.reduce(lambda x, y: x + y, numbers[(len(numbers) // 2):], ""))
        product = 1
        for key in time_dist:
            product *= len(get_win_options(key, time_dist[key]))
        return product
