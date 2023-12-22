from Day import Day


def is_mirror(lines: [str], line: int) -> bool:
    top, bottom = line, line + 1
    equals = []
    while top >= 0 and bottom < len(lines):
        if lines[top] == lines[bottom]:
            equals.append(True)
        else:
            equals.append(False)
        top -= 1
        bottom += 1
    return all(equals) and len(equals) > 0


def find_mirror(pattern: [str], ignore_mirror=None) -> int:
    # First look at rows
    for i in range(len(pattern)):
        if is_mirror(pattern, i) and (ignore_mirror is None or (ignore_mirror is not None and ignore_mirror != 100 * (i + 1))):
            return 100 * (i + 1)
    # Then we transpose for columns
    pattern = [''.join(s) for s in zip(*pattern)]
    for i in range(len(pattern)):
        if is_mirror(pattern, i) and (ignore_mirror is None or (ignore_mirror is not None and ignore_mirror != i + 1)):
            return i + 1
    raise ValueError


def try_modified_patterns(pattern):
    original_mirror = find_mirror(pattern)
    for row in range(len(pattern)):
        for column in range(len(pattern[row])):
            temp_pattern = pattern.copy()
            replacement = '.' if temp_pattern[row][column] == '#' else '#'
            temp_pattern[row] = temp_pattern[row][:column] + replacement + temp_pattern[row][column + 1:]
            try:
                return find_mirror(temp_pattern, ignore_mirror=original_mirror)
            except ValueError:
                continue


class Day13(Day):
    def part1(self, test=False):
        full_input = self.get_input('test' if test else '')
        patterns = [pattern.split('\n') for pattern in full_input.split('\n\n')]
        return sum([find_mirror(pattern) for pattern in patterns])

    def part2(self, test=False):
        full_input = self.get_input('test' if test else '')
        patterns = [pattern.split('\n') for pattern in full_input.split('\n\n')]
        return sum([try_modified_patterns(pattern) for pattern in patterns])
