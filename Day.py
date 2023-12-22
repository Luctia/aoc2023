import re
from abc import ABC, abstractmethod
import pyperclip
import time


class Day(ABC):
    def get_input(self, subtype=None) -> str:
        subtype = subtype if subtype is not None else ""
        filename = re.search(r"Day\d+", self.__str__()).group() + subtype + ".txt"
        file = open("inputs/" + filename, "r")
        result = file.read()
        file.close()
        return result

    def get_input_lines(self, subtype=None) -> [str]:
        return self.get_input(subtype).split("\n")

    @abstractmethod
    def part1(self, test=False):
        raise NotImplementedError

    @abstractmethod
    def part2(self, test=False):
        raise NotImplementedError

    @staticmethod
    def answer(answer):
        pyperclip.copy(str(answer))
        print("Answer: " + str(answer))

    def run_all(self, expected_test_result=None):
        if expected_test_result is not None:
            print("Running tests...")
            total_time = 0
            if expected_test_result[0] is not None:
                try:
                    start_time = time.time()
                    part1_test = self.part1(test=True)
                    end_time = time.time()
                    total_time += end_time - start_time
                    if part1_test != expected_test_result[0]:
                        print("Part 1 test failed (%ss)\n" % (end_time - start_time))
                        return
                except NotImplementedError:
                    print("Part 1 not implemented yet.\n")
            if expected_test_result[1] is not None:
                try:
                    start_time = time.time()
                    part2_test = self.part2(test=True)
                    end_time = time.time()
                    total_time += end_time - start_time
                    if part2_test != expected_test_result[1]:
                        print("Part 2 test failed (%ss)\n" % (end_time - start_time))
                        return
                except NotImplementedError:
                    print("Part 2 not implemented yet.\n")
            print("Tests succeeded! (%ss)\n" % total_time)

        print("Running part 1...")
        start_time = time.time()
        self.answer(self.part1())
        print("(Took %s seconds)\n" % (time.time() - start_time))

        print("Running part 2...")
        start_time = time.time()
        self.answer(self.part2())
        print("(Took %s seconds)\n" % (time.time() - start_time))
