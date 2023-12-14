import typing


def get_input(file_name: str) -> typing.List[typing.List[str]]:
    with open(file_name, "r") as f:
        lines = f.read().split("\n\n")
    return [line.splitlines() for line in lines]


def total(case: typing.List[str], idx: int) -> int:
    return sum(sum(int(a != b) for a, b in zip(x, y)) for x, y in zip(case[idx:], case[idx - 1 :: -1]))


def find_mirror(case: typing.List[str], smudges: int = 0) -> int:
    case_t = list(map("".join, zip(*case)))
    for m, c in ((100, case), (1, case_t)):
        for i in range(1, len(c)):
            if total(c, i) == smudges:
                return m * i
    raise ValueError


def part_a(lines: typing.List[typing.List[str]]) -> int:
    return sum(find_mirror(case) for case in lines)


def part_b(lines: typing.List[typing.List[str]]) -> int:
    return sum(find_mirror(case, 1) for case in lines)


if __name__ == "__main__":
    print(part_a(get_input("../bin/13.txt")))
    print(part_b(get_input("../bin/13.txt")))
