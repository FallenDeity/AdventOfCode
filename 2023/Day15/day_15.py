import dataclasses
import typing
from functools import reduce


@dataclasses.dataclass
class HolidayString:
    data: str

    def __hash__(self) -> int:
        return reduce(lambda x, y: ((x + ord(y)) * 17) % 256, self.data, 0)


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().split(",")
    return lines


def part_a(lines: typing.List[str]) -> int:
    return sum(map(hash, map(HolidayString, lines)))


def part_b(lines: typing.List[str]) -> int:
    data: typing.Dict[int, typing.Dict[str, int]] = {}
    for i in lines:
        if "=" in i:
            s, n = i.split("=")
            data.setdefault(hash(HolidayString(s)), {}).update({s: int(n)})
        else:
            data.get(hash(HolidayString(i[:-1])), {}).pop(i[:-1], None)
    return sum(sum([(n + 1) * i * j for i, j in enumerate(box.values(), start=1)]) for n, box in data.items())


if __name__ == "__main__":
    print(part_a(get_input("../bin/15.txt")))
    print(part_b(get_input("../bin/15.txt")))
