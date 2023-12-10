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
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 'S':
                    # S is an F in both my input and in the testing input. Checking dynamically is possible but messy.
                    loop.append((y, x, 'F'))
                    start = (y, x, 'F')
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
        loop = self.get_loop()
        loopmap = dict()
        for (y, x, z) in loop:
            loopmap[(y, x)] = z
        total = 0
        max_y = max([a[0] for a in loop])
        max_x = max([a[1] for a in loop])
        for y in range(max_y):
            opener = None
            inside = False
            for x in range(max_x):
                tile = loopmap.get((y, x))
                match tile:
                    case None: total += (1 if inside else 0)
                    case '|': inside = not inside
                    case 'F': opener = 'F'
                    case 'L': opener = 'L'
                    case '7': inside = (not inside if opener == 'L' else inside)
                    case 'J': inside = (not inside if opener == 'F' else inside)
                    case _: pass
        return total
