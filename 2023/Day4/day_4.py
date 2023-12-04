from __future__ import annotations

import dataclasses
import typing


@dataclasses.dataclass
class Card:
    id: int
    numbers: typing.List[int]
    winners: typing.List[int]
    value: int = 0

    def __post_init__(self) -> None:
        self.value = 2 ** (len(self.common) - 1) if self.common else 0

    @property
    def common(self) -> typing.Set[int]:
        return set(self.numbers).intersection(self.winners)

    @classmethod
    def parse_card(cls, line: str) -> Card:
        header, numbers = line.split(":")
        id = int(header.split(" ")[-1])
        winners, numbers = numbers.split("|")
        return cls(id, [int(n) for n in numbers.split()], [int(n) for n in winners.split()])


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def part_a(lines: typing.List[str]) -> int:
    return sum([Card.parse_card(line).value for line in lines])


def part_b(lines: typing.List[str]) -> int:
    cards = {c.id: [c] for c in [Card.parse_card(line) for line in lines]}
    for k, v in cards.items():
        copies = {c: cards[c][0] for i in range(k + 1, len(v[0].common) + 1 + k) for c in cards if c == i}
        for i, j in copies.items():
            cards[i].extend([j] * len(cards[k]))
    return sum([len(v) for v in cards.values()])


if __name__ == "__main__":
    print(part_a(get_input("../bin/4.txt")))
    print(part_b(get_input("../bin/4.txt")))
