from Day import Day
import numpy as np


class Day08(Day):
    def part1(self, test=False):
        lines = self.get_input_lines()
        instructions = lines[0]
        mappings = dict()
        for mapping in lines[2:]:
            mappings[mapping[0:3]] = (mapping[7:10], mapping[12:15])
        i = 0
        location = "AAA"
        while location != "ZZZ":
            location = mappings[location][0 if instructions[i % len(instructions)] == "L" else 1]
            i += 1
        return i

    def part2(self, test=False):
        lines = self.get_input_lines()
        instructions = lines[0]
        instr_length = len(instructions)
        mappings = dict()
        results_per_node = dict()
        for mapping in lines[2:]:
            mappings[mapping[0:3]] = (mapping[7:10], mapping[12:15])
            results_per_node[mapping[0:3]] = mapping[0:3]

        for i in range(instr_length):
            for key in results_per_node.keys():
                results_per_node[key] = mappings[results_per_node[key]][0 if instructions[i % len(instructions)] == "L" else 1]

        steps_to_z_per_node = dict()
        for mapping in mappings:
            steps_to_z_per_node[mapping] = (mapping, 0)
        steps = 0
        while any([x[1] == 0 for x in steps_to_z_per_node.values()]):
            steps += instr_length
            for key in [k for k in steps_to_z_per_node if steps_to_z_per_node[k][1] == 0]:
                node = results_per_node[steps_to_z_per_node[key][0]]
                steps_to_z_per_node[key] = (node, -1) if steps_to_z_per_node[key][0] == node else ((node, steps) if node.endswith('Z') else (node, 0))

        a_steps = [steps_to_z_per_node[s] for s in steps_to_z_per_node if s[-1] == 'A']
        res = 1
        for a in a_steps:
            res = np.lcm(res, a[1])
        return res
