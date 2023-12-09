from Day import Day
import numpy as np


class Day09(Day):
    def part1(self, test=False):
        sequences = []
        for line in self.get_input_lines("test" if test else ""):
            sequences.append([int(x) for x in line.split(" ")])
        total = 0
        for sequence in sequences:
            resulting_sequences = []
            while not all([x == 0 for x in sequence[:-1]]):
                resulting_sequences.append(sequence)
                new_sequence = []
                for i in range(1, len(sequence)):
                    new_sequence.append(sequence[i] - sequence[i - 1])
                sequence = new_sequence
            resulting_sequences.append(sequence)
            to_add = 0
            for i in range(len(resulting_sequences) - 1, -1, -1):
                to_add = resulting_sequences[i][-1] + to_add
            total += to_add
        return total

    def part2(self, test=False):
        sequences = []
        for line in self.get_input_lines("test" if test else ""):
            sequences.append([int(x) for x in line.split(" ")])
        total = 0
        for sequence in sequences:
            resulting_sequences = []
            while not all([x == 0 for x in sequence[:-1]]):
                resulting_sequences.append(sequence)
                new_sequence = []
                for i in range(1, len(sequence)):
                    new_sequence.append(sequence[i] - sequence[i - 1])
                sequence = new_sequence
            resulting_sequences.append(sequence)
            to_add = 0
            for i in range(len(resulting_sequences) - 1, -1, -1):
                to_add = resulting_sequences[i][0] - to_add
            total += to_add
        return total
