import typing
from math import prod


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def solve_d(t: float, d: float) -> float:
    return float(v - 1 if (v := (t**2 - 4 * d) ** 0.5) % 1 == 0 else v)


def part_a(lines: typing.List[str]) -> int:
    data = dict(zip(*[map(int, i.split(":")[-1].split()) for i in lines]))
    values = [((k + solve_d(k, v)) // 2) - ((k - solve_d(k, v)) // 2) for k, v in data.items()]
    return int(prod(values))


def part_b(lines: typing.List[str]) -> int:
    data = dict(zip(*[(int("".join(i.split(":")[-1].split())),) for i in lines]))
    values = [((k + solve_d(k, v)) // 2) - ((k - solve_d(k, v)) // 2) for k, v in data.items()]
    return int(prod(values))


if __name__ == "__main__":
    print(part_a(get_input("../bin/6.txt")))
    print(part_b(get_input("../bin/6.txt")))
