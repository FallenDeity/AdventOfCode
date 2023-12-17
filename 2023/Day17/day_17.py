import typing as t
from bisect import insort
from collections import defaultdict, deque

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Point(t.NamedTuple):
    loss: int
    position: t.Tuple[int, int]
    direction: t.Tuple[int, int]
    remaining: int


def get_input(file_name: str) -> t.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def path_find(lines: t.List[str], max_dx: int, min_dx: int) -> int:
    height, width = len(lines), len(lines[0])
    possibilities: t.Deque[Point] = deque()
    for direction in DIRECTIONS[1:3]:
        possibilities.append(Point(0, (0, 0), direction, max_dx))
    seen: t.DefaultDict[t.Tuple[int, int, t.Tuple[int, int], int], float] = defaultdict(lambda: float("inf"))
    while possibilities:
        loss, (y, x), d, r = possibilities.popleft()

        if (y, x) == (height - 1, width - 1) and r <= (max_dx - min_dx):
            return loss

        if r <= (max_dx - min_dx):
            di = DIRECTIONS.index(d)
            for nd in DIRECTIONS[(di + 1) % 4], DIRECTIONS[di - 1]:
                dy, dx = nd
                ny, nx = y + dy, x + dx
                if ny not in range(height) or nx not in range(width):
                    continue
                nr = max_dx - 1
                if seen[ny, nx, nd, nr] <= (nloss := loss + int(lines[ny][nx])):
                    continue
                seen[ny, nx, nd, nr] = nloss
                insort(possibilities, Point(nloss, (ny, nx), nd, nr))

        if r > 0:
            dy, dx = d
            ny, nx = y + dy, x + dx
            if ny not in range(height) or nx not in range(width):
                continue
            nr, nd = r - 1, d
            if seen[ny, nx, nd, nr] <= (nloss := loss + int(lines[ny][nx])):
                continue
            seen[ny, nx, nd, nr] = nloss
            insort(possibilities, Point(nloss, (ny, nx), nd, nr))

    return -1


def part_a(lines: t.List[str]) -> int:
    max_dx, min_dx = 3, 0
    return path_find(lines, max_dx, min_dx)


def part_b(lines: t.List[str]) -> int:
    max_dx, min_dx = 10, 4
    return path_find(lines, max_dx, min_dx)


if __name__ == "__main__":
    print(part_a(get_input("../bin/17.txt")))
    print(part_b(get_input("../bin/17.txt")))
