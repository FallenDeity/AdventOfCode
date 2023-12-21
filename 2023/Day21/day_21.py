import typing
from collections import deque


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def print_garden(garden: typing.List[str], positions: typing.Sequence[typing.Tuple[int, int]]) -> None:
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if (i, j) in positions:
                print("O", end="")
            else:
                print(garden[i][j], end="")
        print()


def part_a(garden: typing.List[str], steps: int = 64) -> int:
    x_l, y_l = len(garden), len(garden[0])
    r, c = [(i, j) for i in range(len(garden)) for j in range(len(garden[0])) if garden[i][j] == "S"][0]
    queue = deque([(r, c, 0)])
    visited = set()
    step_map: typing.Dict[int, typing.Set[typing.Tuple[int, int]]] = {}
    while queue:
        row, col, step = queue.popleft()
        if (row, col) not in visited and step <= steps:
            visited.add((row, col))
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + direction[0], col + direction[1]
                if garden[new_row % x_l][new_col % y_l] != "#":
                    queue.append((new_row, new_col, step + 1))
                    visited.discard((new_row, new_col))
                    step_map.setdefault(step + 1, set()).add((new_row, new_col))
    return len(step_map[steps])


def part_b(garden: typing.List[str], steps: int = 26501365) -> int:
    # grid is a square, so the pattern repeats after 65 steps at 64 steps its 1 step shy from the edge
    # the edge also has no walls, so the pattern is the same for all steps after 65
    a0 = 3848  # part_a(garden, 65)
    a1 = 34310  # part_a(garden, 65 + 131)
    a2 = 95144  # part_a(garden, 65 + 131 * 2)
    b0, b1, b2 = a0, a1 - a0, a2 - a1
    n = (steps - 65) // len(garden)
    return b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)


if __name__ == "__main__":
    print(part_a(get_input("../bin/21.txt")))
    print(part_b(get_input("../bin/21.txt")))
