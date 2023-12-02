from __future__ import annotations

import dataclasses
import typing


@dataclasses.dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __le__(self, other: Round) -> bool:
        if not isinstance(other, Round):
            raise TypeError(f"Cannot compare Round to {type(other)}")
        return self.red <= other.red and self.green <= other.green and self.blue <= other.blue

    @classmethod
    def from_str(cls, line: str) -> Round:
        data = line.strip().replace(",", "").split(" ")
        return cls(**{data[i + 1]: int(data[i]) for i in range(0, len(data), 2)})

    @property
    def product(self) -> int:
        return self.red * self.green * self.blue


THRESHOLD = Round(red=12, green=13, blue=14)


@dataclasses.dataclass
class Game:
    game_id: int
    rounds: typing.List[Round]

    @classmethod
    def from_str(cls, line: str) -> Game:
        game, data = line.split(":")
        game_id = int(game[5:])
        rounds = [Round.from_str(round) for round in data.split(";")]
        return cls(game_id=game_id, rounds=rounds)

    @property
    def max_round(self) -> Round:
        max_round = Round()
        for round in self.rounds:
            max_round.red = max(max_round.red, round.red)
            max_round.green = max(max_round.green, round.green)
            max_round.blue = max(max_round.blue, round.blue)
        return max_round

    @property
    def is_valid(self) -> bool:
        return self.max_round <= THRESHOLD


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def part_a(games: typing.List[Game]) -> int:
    return sum([game.game_id for game in games if game.is_valid])


def part_b(games: typing.List[Game]) -> int:
    return sum([game.max_round.product for game in games])


if __name__ == "__main__":
    inp = get_input("../bin/2.txt")
    games = [Game.from_str(line) for line in inp]
    print(part_a(games), part_b(games))

    data = []
    for i in range(3):
        p = __import__("random").sample(inp, 10)
        test = [Game.from_str(line) for line in p]
        data.append(
            (
                p,
                part_b(test),
            )
        )
    print(data)
