from Day import Day


def get_winning_numbers(ticket):
    return [int(num) for num in ticket.split(": ")[1].split(" |")[0].split(" ") if num]


def get_actual_numbers(ticket):
    return [int(num) for num in ticket.split("| ")[1].split(" ") if num]


def get_card_number(card):
    return int(card.split( )[1].split(":")[0])


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def get_next_cards(base_card, number_of_cards, all_cards):
    next_cards = []
    for i in range(base_card, number_of_cards + base_card):
        next_cards.append(get_card_number(all_cards[i]))
    return next_cards


class Day04(Day):
    def part1(self):
        data = self.get_input_lines()
        totalpoints = 0
        for ticket in data:
            winning_numbers = get_winning_numbers(ticket)
            actual_numbers = get_actual_numbers(ticket)
            matching = len(intersection(winning_numbers, actual_numbers))
            if matching > 1:
                totalpoints += 2**(matching - 1)
            if matching == 1:
                totalpoints += 1
        self.answer(totalpoints)

    def part2(self):
        number_of_wins = dict()
        lines = self.get_input_lines()
        resulting_cards = []
        for line in lines:
            card_number = get_card_number(line)
            resulting_cards.append(card_number)
            winning_numbers = get_winning_numbers(line)
            actual_numbers = get_actual_numbers(line)
            matching = len(intersection(winning_numbers, actual_numbers))
            number_of_wins[card_number] = matching
        i = 0
        while i < len(resulting_cards):
            card_number = resulting_cards[i]
            wins = number_of_wins[card_number]
            for card in get_next_cards(card_number, wins, lines):
                resulting_cards.append(card)
            i += 1
        self.answer(len(resulting_cards))
