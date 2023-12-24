import re
from ordered_set import OrderedSet
from Day import Day


def get_hash(text: str) -> int:
    current = 0
    for c in text:
        current += ord(c)
        current *= 17
        current %= 256
    return current


class Day15(Day):
    def part1(self, test=False):
        return sum([get_hash(code) for code in self.get_input_lines('test' if test else '')[0].split(',')])

    def part2(self, test=False):
        boxes = dict()
        lenses = dict()
        for code in self.get_input_lines('test' if test else '')[0].split(','):
            lens = re.search(r'\w+', code).group()
            box = get_hash(lens)
            if '=' in code:
                focal_length = int(code[-1])
                lenses[lens] = focal_length
                if box in boxes.keys():
                    existing = boxes[box]
                    existing.add(lens)
                    boxes[box] = existing
                else:
                    boxes[box] = OrderedSet([lens])
            else:
                if box in boxes.keys():
                    existing = boxes[box]
                    if lens in existing:
                        existing.remove(lens)
                        boxes[box] = existing

        total = 0
        for box in boxes.keys():
            for slot in range(len(boxes[box])):
                lens = boxes[box][slot]
                total += (1 + box) * (slot + 1) * lenses[lens]
        return total
