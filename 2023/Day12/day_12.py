import dataclasses
import enum
import typing
from functools import lru_cache


class STATES(enum.Enum):
    WORKING = "."
    DAMAGED = "#"
    UKNOWN = "?"

    def __str__(self) -> str:
        return self.value


@dataclasses.dataclass(frozen=True)
class Row:
    id: int
    springs: str
    damages: tuple[int, ...]

    @lru_cache(maxsize=None)
    def check(self, line: str, required: tuple[int, ...]) -> int:
        if not required:
            return str(STATES.DAMAGED) not in line
        s, current = 0, required[0]
        for i in range(len(line) - sum(required) - len(required) + 2):
            if str(STATES.DAMAGED) in line[:i] or line[i + current :].startswith(str(STATES.DAMAGED)):
                continue
            segment = line[i : i + current]
            if not all(c in (str(STATES.UKNOWN), str(STATES.DAMAGED)) for c in segment):
                continue
            s += self.check(line[i + current + 1 :], required[1:])
        return s

    @property
    def possible(self) -> int:
        return self.check(self.springs, self.damages)

    @classmethod
    def from_str(cls, id: int, row: str, *, folded: bool = False) -> "Row":
        data, nums = row.split(" ")
        line = str(STATES.UKNOWN).join(data for _ in range(5 if folded else 1))
        return cls(id, line, tuple([int(n) for n in nums.split(",")] * (5 if folded else 1)))


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def part_a(lines: typing.List[str]) -> int:
    rows = [Row.from_str(n, line) for n, line in enumerate(lines, start=1)]
    return sum([row.possible for row in rows])


def part_b(lines: typing.List[str]) -> int:
    rows = [Row.from_str(n, line, folded=True) for n, line in enumerate(lines, start=1)]
    return sum([row.possible for row in rows])


if __name__ == "__main__":
    print(part_a(get_input("../bin/12.txt")))
    print(part_b(get_input("../bin/12.txt")))
