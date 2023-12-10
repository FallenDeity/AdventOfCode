import re
import typing
from queue import SimpleQueue


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def offsets(c: str) -> typing.Tuple[typing.Tuple[int, int], ...]:
    return {
        "|": ((1, 0), (-1, 0)),
        "-": ((0, 1), (0, -1)),
        "L": ((-1, 0), (0, 1)),
        "J": ((-1, 0), (0, -1)),
        "7": ((1, 0), (0, -1)),
        "F": ((1, 0), (0, 1)),
        ".": tuple(),
        "S": ((1, 0), (0, 1), (-1, 0), (0, -1)),
    }[c]


def part_a(start: typing.Tuple[int, int], maze: typing.List[str]) -> typing.Dict[typing.Tuple[int, int], int]:
    qu = SimpleQueue[typing.Tuple[int, int]]()
    dist = {start: 0}
    qu.put(start)

    for sc in "|-LJ7F":
        flag = 0
        for dx, dy in offsets(sc):
            near = maze[start[0] + dx][start[1] + dy]
            if ((not dx) and ((dx, -dy) in offsets(near))) or ((not dy) and ((-dx, dy) in offsets(near))):
                flag += 1
        if flag == 2:
            maze[start[0]] = maze[start[0]].replace("S", sc)

    while not qu.empty():
        p = qu.get()
        for dx, dy in offsets(maze[p[0]][p[1]]):
            nx, ny = p[0] + dx, p[1] + dy
            if (nx, ny) not in dist:
                dist[(nx, ny)] = dist[p] + 1
                qu.put((nx, ny))
    return dist


def part_b(dist: typing.Dict[typing.Tuple[int, int], int], maze: typing.List[str]) -> int:
    loop_maze = ["".join([c if (i, j) in dist else "." for j, c in enumerate(row)]) for i, row in enumerate(maze)]
    cnt = 0
    for row in loop_maze:
        l_walls = 0
        row = re.sub(r"L-*7|F-*J", r"|", row)
        row = re.sub(r"L-*J|F-*7", r"", row)
        for c in row:
            if c == "|":
                l_walls += 1
            elif c == ".":
                cnt += l_walls % 2
    return cnt


if __name__ == "__main__":
    lines = get_input("../bin/10.txt")
    lines = ["." * len(lines[0])] + lines + ["." * len(lines[0])]
    start = [(i, row.find("S")) for i, row in enumerate(lines) if row.find("S") != -1][0]
    dist = part_a(start, lines)
    print(max(dist.values()))
    print(part_b(dist, lines))
