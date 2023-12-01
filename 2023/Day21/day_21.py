import typing


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def part_a(lines: typing.List[str]) -> int:
    return 0


def part_b(lines: typing.List[str]) -> int:
    return 0


if __name__ == "__main__":
    print(part_a(get_input("../bin/21.txt")))
    print(part_b(get_input("../bin/21.txt")))
