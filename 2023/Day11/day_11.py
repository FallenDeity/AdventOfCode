import typing


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def expand(universe: typing.List[str], factor: float) -> int:
    row_distance, total_distance = 0.0, 0.0
    seen_galaxies, space = 0.0, 0.0
    for count in map(lambda x: x.count("#"), universe):
        row_distance += seen_galaxies * space
        total_distance += row_distance * count
        seen_galaxies += count
        space = 1 if count else factor
    return int(total_distance)


def part_a(lines: typing.List[str]) -> int:
    return expand(lines, 2) + expand(["".join(i) for i in zip(*lines)], 2)


def part_b(lines: typing.List[str]) -> int:
    return expand(lines, 1e6) + expand(["".join(i) for i in zip(*lines)], 1e6)


if __name__ == "__main__":
    print(part_a(get_input("../bin/11.txt")))
    print(part_b(get_input("../bin/11.txt")))
