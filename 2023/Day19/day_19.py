from __future__ import annotations

import dataclasses
import re
import typing
from math import prod


@dataclasses.dataclass
class Workflow:
    name: str
    data: typing.Dict[str, str]
    final: str

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, str):
            return self.name == __value
        if isinstance(__value, Workflow):
            return self.name == __value.name
        return False

    @classmethod
    def from_str(cls, s: str) -> Workflow:
        name, data = s.split("{")
        body = dict(i.split(":") for i in data.split(",")[:-1])
        return cls(name, body, data.split(",")[-1][:-1])

    def evaluate_part(self, part: "Part") -> str:
        common_keys = [(i, j) for j in self.data.keys() for i in part.data.keys() if i in j]
        for key, check in common_keys:
            value = part.data[key]
            if eval(check.replace(key, str(value))):
                return self.data[check]
        return self.final


@dataclasses.dataclass
class Part:
    data: typing.Dict[str, int]

    @classmethod
    def from_str(cls, s: str) -> Part:
        return cls({k: int(v) for k, v in re.findall(r"(\w)=(\d+)", s)})

    @property
    def value(self) -> int:
        return sum(self.data.values())


def get_input(file_name: str) -> typing.Tuple[typing.List[Workflow], typing.List[Part]]:
    with open(file_name, "r") as f:
        lines = f.read()
    workflows, parts = lines.split("\n\n")
    return list(map(Workflow.from_str, workflows.split("\n"))), list(map(Part.from_str, parts.split("\n")))


def part_a(lines: typing.Tuple[typing.List[Workflow], typing.List[Part]]) -> int:
    workflows, parts = lines
    accepted = []
    while parts:
        workflow = workflows[workflows.index("in")]  # type: ignore
        part = parts.pop(0)
        while True:
            value = workflow.evaluate_part(part)
            if value in "AR":
                accepted += [part] if value == "A" else []
                break
            workflow = workflows[workflows.index(value)]  # type: ignore
    return sum([part.value for part in accepted])


def part_b(lines: typing.Tuple[typing.List[Workflow], typing.List[Part]]) -> int:
    workflows, *_ = lines
    s = 0
    remaining = [("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]
    while remaining:
        data, values = remaining.pop(0)
        if data.lower() != data:
            if data == "A":
                s += prod(b - a + 1 for a, b in values.values())
            continue
        workflow = workflows[workflows.index(data)]  # type: ignore
        for rule in workflow.data:
            checked = rule[0]
            num = int(rule[2:])
            lo, hi = values[checked]
            v_map = {"<": (lo, num - 1), ">": (num + 1, hi)}
            remaining.append((workflow.data[rule], {**values, checked: v_map[rule[1]]}))
            values[checked] = (num, hi) if rule[1] == "<" else (lo, num)
        else:
            remaining.append((workflow.final, values))
    return s


if __name__ == "__main__":
    print(part_a(get_input("../bin/19.txt")))
    print(part_b(get_input("../bin/19.txt")))
