from Day import Day


class Brick:
    xs: [int]
    ys: [int]
    zs: [int]


def drop_bricks(bricks: [Brick]) -> [Brick]:
    pass


class Day22(Day):
    def part1(self, test=False):
        lines = self.get_input_lines('test' if test else '')
        bricks = drop_bricks(lines)

        # go bottom up. if there is no brick directly under the current brick, don't move. otherwise, move

        # go top down. if for a brick, there is only one supporting brick, remove the supporting
        #  brick from possibilities

    def part2(self, test=False):
        pass
