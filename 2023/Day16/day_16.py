import typing

DIRECTIONS = typing.Literal["R", "L", "U", "D"]
REFLECT_MAP: typing.Dict[str, typing.Dict[DIRECTIONS, DIRECTIONS]] = {
    "/": {"R": "U", "L": "D", "U": "R", "D": "L"},
    "\\": {"R": "D", "L": "U", "U": "L", "D": "R"},
}
SPLIT_MAP: typing.Dict[str, typing.Tuple[DIRECTIONS, ...]] = {"|": ("R", "L"), "-": ("U", "D")}
POS_MAP: typing.Dict[DIRECTIONS, typing.Tuple[int, int]] = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}


class Beam(typing.NamedTuple):
    i: int
    j: int
    direction: DIRECTIONS


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def validate_beams(lines: typing.List[str], beams: typing.List[Beam]) -> typing.List[Beam]:
    return [Beam(i, j, direction) for i, j, direction in beams if 0 <= i < len(lines) and 0 <= j < len(lines[0])]


def part_a(lines: typing.List[str], start: Beam = Beam(0, 0, "R")) -> int:
    energized = set()
    done = set()
    beams = [start]
    while beams:
        x, y, direction = beams.pop()
        done.add(Beam(x, y, direction))
        while 0 <= x < len(lines) and 0 <= y < len(lines[0]):
            energized.add((x, y))
            if lines[x][y] in "/\\":
                direction = REFLECT_MAP[lines[x][y]][direction]
                x, y = x + POS_MAP[direction][0], y + POS_MAP[direction][1]
            elif lines[x][y] in "|-":
                if direction in SPLIT_MAP[lines[x][y]]:
                    dirs = {k: v for k, v in POS_MAP.items() if k not in SPLIT_MAP[lines[x][y]]}
                    beams.extend([Beam(x + v[0], y + v[1], k) for k, v in dirs.items()])
                    break
                x, y = x + POS_MAP[direction][0], y + POS_MAP[direction][1]
            elif lines[x][y] == ".":
                x, y = x + POS_MAP[direction][0], y + POS_MAP[direction][1]
        beams = [i for i in validate_beams(lines, beams) if i not in done]
    return len(energized)


def part_b(lines: typing.List[str]) -> int:
    max_energy = []
    for i in range(len(lines)):
        max_energy.append(part_a(lines, Beam(i, 0, "R")))
        max_energy.append(part_a(lines, Beam(i, len(lines[0]) - 1, "L")))
    for j in range(len(lines[0])):
        max_energy.append(part_a(lines, Beam(0, j, "D")))
        max_energy.append(part_a(lines, Beam(len(lines) - 1, j, "U")))
    return max(max_energy)


if __name__ == "__main__":
    print(part_a(get_input("../bin/16.txt")))
    print(part_b(get_input("../bin/16.txt")))
