from Day import Day
from functools import cmp_to_key
from collections import Counter


def get_card_number(card, joker=False):
    match card:
        case 'A': return 14
        case 'K': return 13
        case 'Q': return 12
        case 'J': return 1 if joker else 11
        case 'T': return 10
        case _: return int(card)


def compare_on_high_card(hand1, hand2, joker=False):
    i = 0
    score1 = get_card_number(hand1[0][i], joker)
    score2 = get_card_number(hand2[0][i], joker)
    while score2 == score1 and i < 5:
        i += 1
        score1 = get_card_number(hand1[0][i], joker)
        score2 = get_card_number(hand2[0][i], joker)
    if score1 > score2:
        return 1
    if score2 > score1:
        return -1
    raise NotImplementedError


def get_score(hand_map, joker=False):
    amounts = hand_map.values()
    if joker and hand_map.keys().__contains__('J'):
        no_of_js = hand_map['J']
        hand_map['J'] = 0
        amounts = sorted(hand_map.values(), reverse=True)
        amounts[0] += no_of_js
    if 5 in amounts:
        return 6
    if 4 in amounts:
        return 5
    if 3 in amounts:
        if 2 in amounts:
            return 4
        return 3
    if 2 in amounts:
        if len(list(filter(lambda x: x == 2, amounts))) == 2:
            return 2
        return 1
    return 0


def compare_hands(hand1, hand2):
    hand1_map = dict(Counter(hand1[0]))
    hand2_map = dict(Counter(hand2[0]))
    score1 = get_score(hand1_map)
    score2 = get_score(hand2_map)
    if score1 > score2:
        return 1
    if score1 < score2:
        return -1
    return compare_on_high_card(hand1, hand2)


def compare_hands2(hand1, hand2):
    hand1_map = dict(Counter(hand1[0]))
    hand2_map = dict(Counter(hand2[0]))
    score1 = get_score(hand1_map, True)
    score2 = get_score(hand2_map, True)
    if score1 > score2:
        return 1
    if score1 < score2:
        return -1
    return compare_on_high_card(hand1, hand2, True)


class Day07(Day):
    def part1(self, test=False):
        hbs = [(hb.split(" ")[0], hb.split(" ")[1]) for hb in self.get_input_lines("test" if test else "")]
        hbs = sorted(hbs, key=cmp_to_key(compare_hands))
        return sum([(i + 1) * int(hb[1]) for i, hb in enumerate(hbs)])

    def part2(self, test=False):
        hbs = [(hb.split(" ")[0], hb.split(" ")[1]) for hb in self.get_input_lines("test" if test else "")]
        hbs = sorted(hbs, key=cmp_to_key(compare_hands2))
        return sum([(i + 1) * int(hb[1]) for i, hb in enumerate(hbs)])
