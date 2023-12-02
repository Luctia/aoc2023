def get_game_hands(game):
    game = game.split(":")[1][1:-1]
    hands = game.split("; ")
    return hands


def get_rgb(hand):
    red = 0
    green = 0
    blue = 0
    colors = hand.split(", ")
    for color in colors:
        number = int(color.split(" ")[0])
        col = color.split(" ")[1]
        if col == 'blue' and number > blue:
            blue = number
        if col == 'red' and number > red:
            red = number
        if col == 'green' and number > green:
            green = number
    return red, green, blue


def get_min_colors(game):
    red = 0
    green = 0
    blue = 0
    hands = get_game_hands(game)
    for hand in hands:
        colors = get_rgb(hand)
        if colors[0] > red:
            red = colors[0]
        if colors[1] > green:
            green = colors[1]
        if colors[2] > blue:
            blue = colors[2]
    return red, green, blue


def qualifies(game):
    min_colors = get_min_colors(game)
    return min_colors[0] <= 12 and min_colors[1] <= 13 and min_colors[2] <= 14


def part1():
    with open("inputs/day2.txt") as data:
        sum = 0
        for line in data:
            if qualifies(line):
                sum += int(line.split(" ")[1].split(":")[0])
        return sum


def get_power(game):
    min_colors = get_min_colors(game)
    return min_colors[0] * min_colors[1] * min_colors[2]


def part2():
    with open("inputs/day2.txt") as data:
        sum = 0
        for line in data:
            sum += get_power(line)
        return sum
