import re
from abc import ABC, abstractmethod
import pyperclip


class Day(ABC):
    def get_input(self, subtype=None):
        subtype = subtype if subtype is not None else ""
        filename = re.search(r"Day\d+", self.__str__()).group() + subtype + ".txt"
        file = open("inputs/" + filename, "r")
        result = file.read()
        file.close()
        return result

    def get_input_lines(self, subtype=None):
        return self.get_input(subtype).split("\n")

    @abstractmethod
    def part1(self):
        raise NotImplementedError

    @abstractmethod
    def part2(self):
        raise NotImplementedError

    @staticmethod
    def answer(answer):
        pyperclip.copy(str(answer))
        print("Answer: " + str(answer) + "\n")
