from Day import Day


def get_connected(coordinate, grid):
    match coordinate[2]:
        case 'F': to_check = [(coordinate[0] + 1, coordinate[1]), (coordinate[0], coordinate[1] + 1)]
        case 'J': to_check = [(coordinate[0] - 1, coordinate[1]), (coordinate[0], coordinate[1] - 1)]
        case '|': to_check = [(coordinate[0] - 1, coordinate[1]), (coordinate[0] + 1, coordinate[1])]
        case '-': to_check = [(coordinate[0], coordinate[1] + 1), (coordinate[0], coordinate[1] - 1)]
        case 'L': to_check = [(coordinate[0] - 1, coordinate[1]), (coordinate[0], coordinate[1] + 1)]
        case '7': to_check = [(coordinate[0] + 1, coordinate[1]), (coordinate[0], coordinate[1] - 1)]
        case _: raise NotImplementedError
    return [(y, x, grid[y][x]) for y, x in to_check]


class Day10(Day):
    def get_loop(self, test=False):
        grid = self.get_input_lines("test" if test else "")
        loop = []
        start = None
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 'S':
                    # S in an F in both my input and in the testing input. Checking dynamically is possible but messy.
                    loop.append((y, x, '7'))
                    start = (y, x, '7')
        connected = get_connected(loop[0], grid)
        loop = [connected[0]] + loop + [connected[1]]
        while True:
            connected = get_connected(loop[-1], grid)
            if connected[0] not in loop:
                loop.append(connected[0])
                continue
            if connected[1] not in loop:
                loop.append(connected[1])
                continue
            break
        return loop

    def part1(self, test=False):
        return len(self.get_loop(test)) / 2

    def part2(self, test=False):
        loop = self.get_loop(True)
        total = 0
        # opening = ['|', 'J', '7'] ADDED -5
        # closing = ['|', 'F', 'L']
        for y in range(max([a[0] for a in loop])):
            closed = True
            in_line = sorted([(c[1], c[2]) for c in loop if c[0] == y])
            i = 0
            opened_at = 0
            while i < len(in_line) - 1:
                # if in_line[i][0] != in_line[i + 1][0] - 1 and closed:
                #     # The tile we're checking has nothing to the right, and we are currently not opened, so it opens.
                #     closed = False
                #     opened_at = in_line[i][0] + 1
                #     # total += in_line[i + 1][0] - in_line[i][0] - 1
                #     continue
                if in_line[i][1] == '|':
                    # Found a pipe, open or close.
                    if closed:
                        closed = False
                        opened_at = in_line[i][0] + 1
                    else:
                        closed = True
                        total += in_line[i][0] - opened_at
                    i += 1
                    continue
                if in_line[i][0] == in_line[i + 1][0] - 1:
                    # We have two characters next to each other. These (and potentially following) could be a line:
                    # L---7, L7
                    # Or self-enclosed:
                    # F7, L-----J
                    # In the case that it is a line, we want to open or close.
                    start_i = i
                    if in_line[i][1] == 'L':
                        i += 1
                        while in_line[i][1] not in ['J', '7']:
                            i += 1
                        if in_line[i][1] == 'J':
                            # This is an L followed by a J: self enclosed.
                            if not closed:
                                # We were open, so we should remain open, but we should make sure this part doesn't
                                #  count.
                                total -= (in_line[i][0] - in_line[start_i][0] + 1)
                        if in_line[i][1] == '7':
                            # This is an L followed by a 7: it is a line. We should toggle open/closed.
                            if closed:
                                closed = False
                                opened_at = in_line[i][0] + 1
                            else:
                                # We were open, so we should close but also count.
                                closed = True
                                total += in_line[start_i][0] - opened_at
                    if in_line[i][1] == 'F':
                        i += 1
                        while in_line[i][1] not in ['J', '7']:
                            i += 1
                        if in_line[i][1] == '7':
                            # This is an F followed by a 7: self enclosed.
                            if not closed:
                                # We were open, so we should remain open, but we should make sure this part doesn't
                                #  count.
                                total -= (in_line[i][0] - in_line[start_i][0] + 1)
                        if in_line[i][1] == 'J':
                            # This is an F followed by a J: it is a line. We should toggle open/closed.
                            if closed:
                                closed = False
                                opened_at = in_line[i][0] + 1
                            else:
                                # We were open, so we should close but also count.
                                closed = True
                                total += in_line[start_i][0] - opened_at
                    i += 1
        return total
        # too low  410
        # too high 889
