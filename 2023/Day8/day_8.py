from __future__ import annotations

import dataclasses
import itertools
import math
import typing


@dataclasses.dataclass
class Node:
    name: str
    left: str
    right: str

    def __getitem__(self, item: int) -> str:
        return self.left if item == 0 else self.right

    @classmethod
    def from_str(cls, s: str) -> Node:
        name, data = s.split(" = ")
        left, right = data[1:-1].split(", ")
        return cls(name, left, right)


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def network(lines: typing.List[str]) -> typing.Dict[str, Node]:
    return {line.split(" = ")[0]: Node.from_str(line) for line in lines}


def part_a(lines: typing.List[str], current: str, condition: typing.Callable[[str], bool]) -> int:
    instructions, _, paths = lines[0], lines[1], network(lines[2:])
    for n, instruction in enumerate(itertools.cycle(instructions), start=1):
        current = paths[current]["LR".find(instruction)]
        if condition(current):
            return n
    return -1  # No solution found, should never happen


def part_b(lines: typing.List[str]) -> int:
    starting = [node for node in network(lines[2:]) if node[2] == "A"]
    times = [part_a(lines, node, lambda x: x[2] == "Z") for node in starting]
    return math.lcm(*times)


if __name__ == "__main__":
    print(part_a(get_input("../bin/8.txt"), current="AAA", condition=lambda x: x == "ZZZ"))
    print(part_b(get_input("../bin/8.txt")))
