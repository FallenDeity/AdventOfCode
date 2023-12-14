import functools
import typing
from itertools import count

ROW = typing.Tuple[str, ...]


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


@functools.cache
def rotate(lines: typing.Tuple[ROW, ...]) -> typing.Tuple[ROW, ...]:
    return tuple(x[::-1] for x in zip(*lines))


@functools.cache
def fall(lines: typing.Tuple[ROW, ...]) -> typing.Tuple[ROW, ...]:
    new_lines = []
    for col in zip(*lines):
        new_col = ["."] * len(col)
        new_lines.append(new_col)
        i = 0
        for y, c in enumerate(col, start=1):
            if c == "#":
                new_col[y - 1] = c
                i = y
            if c == "O":
                new_col[i] = c
                i += 1
    return tuple(zip(*new_lines))


@functools.cache
def cycle_lines(lines: typing.Tuple[ROW, ...]) -> typing.Tuple[ROW, ...]:
    for _ in range(4):
        lines = rotate(fall(lines))
    return lines


def calculate_load(lines: typing.Tuple[ROW, ...]) -> int:
    return sum(y * row.count("O") for y, row in enumerate(reversed(lines), 1))


def part_a(lines: typing.Tuple[ROW, ...]) -> int:
    return calculate_load(fall(lines))


def part_b(lines: typing.Tuple[ROW, ...]) -> int:
    tortoise = hare = lines
    for i in count(1):
        tortoise = cycle_lines(tortoise)
        hare = cycle_lines(cycle_lines(hare))
        if tortoise == hare:
            break
    cycle_length, initial = i, 2 * i
    n = 1000000000
    for _ in range((n - initial) % cycle_length):
        tortoise = cycle_lines(tortoise)
    return calculate_load(tortoise)


if __name__ == "__main__":
    print(part_a(tuple(map(tuple, get_input("../bin/14.txt")))))
    print(part_b(tuple(map(tuple, get_input("../bin/14.txt")))))
