from __future__ import annotations

import dataclasses
import typing

SYMBOLS = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~".replace(".", "")


@dataclasses.dataclass
class Cell:
    value: str
    row: int
    span: tuple[int, int]
    is_symbol: bool = False

    def __int__(self) -> int:
        return int(self.value) if not self.is_symbol else 0

    def is_adjacent(self, cell: Cell) -> bool:
        return (
            cell is not self
            and cell.row in range(self.row - 1, self.row + 2)
            and self.span[0] in range(cell.span[0] - 1, cell.span[1] + 1)
        )


def parse_cells(data: list[str]) -> list[Cell]:
    cells: list[Cell] = []
    for y, row in enumerate(data):
        values = [Cell(m, y, (n, n + 1), True) for n, m in enumerate(row) if m in SYMBOLS]
        for n, m in enumerate(row):
            if m.isdigit() and not (n > 0 and row[n - 1].isdigit()):
                end = [i for i, c in enumerate(row[n:]) if not c.isdigit()] or [len(row) - n]
                values.append(Cell(row[n : n + end[0]], y, (n, n + end[0])))
        cells.extend(values)
    return cells


def get_adjacent(cell: Cell, cells: list[Cell]) -> list[Cell]:
    return [c for c in cells if cell.is_adjacent(c)]


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def part_a(cells: list[Cell]) -> int:
    return sum(sum([[int(c) for c in get_adjacent(c, cells)] for c in cells if c.is_symbol], []))


def part_b(cells: list[Cell]) -> int:
    return sum([int(g[0]) * int(g[1]) for c in cells if c.value == "*" and len((g := get_adjacent(c, cells))) == 2])


if __name__ == "__main__":
    cells = parse_cells(get_input("../bin/3.txt"))
    print(part_a(cells))
    print(part_b(cells))
