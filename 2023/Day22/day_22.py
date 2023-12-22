import dataclasses
import typing
from collections import defaultdict


@dataclasses.dataclass
class Cube:
    x: int
    y: int
    z: int


@dataclasses.dataclass
class Brick:
    start: Cube
    end: Cube

    @property
    def positions(self) -> typing.List[typing.Tuple[int, int, int]]:
        return [
            (x, y, z)
            for x in range(self.start.x, self.end.x + 1)
            for y in range(self.start.y, self.end.y + 1)
            for z in range(self.start.z, self.end.z + 1)
        ]

    @classmethod
    def from_str(cls, s: str) -> "Brick":
        return cls(*[Cube(*map(int, c.split(","))) for c in s.split("~")])


def get_input(file_name: str) -> typing.List[Brick]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return [Brick.from_str(line) for line in lines]


def drop_brick(tallest: typing.Dict[typing.Tuple[int, int], int], brick: Brick) -> Brick:
    dz = max(brick.start.z - max(tallest[(x, y)] for (x, y, _) in brick.positions) - 1, 0)
    return Brick(*[Cube(c.x, c.y, c.z - dz) for c in (brick.start, brick.end)])


def simulate_fall(bricks: typing.List[Brick]) -> typing.Tuple[int, typing.List[Brick]]:
    occupied: typing.Dict[typing.Tuple[int, int], int] = defaultdict(int)
    stack: typing.List[Brick] = []
    falls = 0
    for brick in bricks:
        new_brick = drop_brick(occupied, brick)
        falls += new_brick.start.z != brick.start.z
        stack.append(new_brick)
        for x, y, _ in new_brick.positions:
            occupied[(x, y)] = new_brick.end.z
    return falls, stack


def solve(data: typing.List[Brick]) -> typing.Tuple[int, int]:
    bricks = sorted(data, key=lambda x: x.start.z)
    _, stack = simulate_fall(bricks)
    p1 = p2 = 0
    for i in range(len(stack)):
        removed = stack[:i] + stack[i + 1 :]
        falls, _ = simulate_fall(removed)
        p1 += 1 if not falls else 0
        p2 += falls
    return p1, p2


def part_a(lines: typing.List[Brick]) -> int:
    return solve(lines)[0]


def part_b(lines: typing.List[Brick]) -> int:
    return solve(lines)[1]


if __name__ == "__main__":
    print(part_a(get_input("../bin/22.txt")))
    print(part_b(get_input("../bin/22.txt")))
