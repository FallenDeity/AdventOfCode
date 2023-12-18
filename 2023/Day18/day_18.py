import itertools
import typing


class Trench(typing.NamedTuple):
    direction: tuple[int, int]
    length: int
    c_dir: tuple[int, int]
    color: int


def get_input(file_name: str) -> typing.List[Trench]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return list(
        itertools.starmap(
            lambda dir, n, col: Trench(
                [(0, -1), (0, 1), (-1, 0), (1, 0)]["UDLR".index(dir)],
                int(n),
                [(1, 0), (0, 1), (-1, 0), (0, -1)][int(col[-2])],  # RDLU
                int(col[2:-2], 16),
            ),
            map(str.split, lines),
        )
    )


def draw(points: typing.List[typing.Tuple[int, int]]) -> int:
    return abs(sum(p1[0] * p2[1] - p1[1] * p2[0] for p1, p2 in zip(points, points[1:] + points[:1])) // 2)


def part_a(data: typing.List[Trench]) -> int:
    points = [(0, 0)]
    for (dx, dy), n, *_ in data:
        x, y = points[-1]
        points.append((x + dx * n, y + dy * n))
    return draw(points) + sum(d[1] for d in data) // 2 + 1


def part_b(data: typing.List[Trench]) -> int:
    return part_a(list(itertools.starmap(lambda a, b, c, d: Trench(c, d, a, b), data)))


if __name__ == "__main__":
    print(part_a(get_input("../bin/18.txt")))
    print(part_b(get_input("../bin/18.txt")))
