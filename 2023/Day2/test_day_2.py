import typing

import pytest
from day_2 import Game, part_a, part_b


@pytest.mark.parametrize(
    "game, expected",
    zip(
        [
            "Game 1: 4 green, 7 blue; 2 blue, 4 red; 5 blue, 2 green, 2 red; 1 green, 3 red, 9 blue; 3 green, 9 blue; 7 green, 2 blue, 2 red",
            "Game 2: 1 blue, 2 red; 1 green, 2 blue, 1 red; 1 red, 5 green; 3 red, 2 blue, 8 green; 3 blue, 2 red, 4 green; 2 blue, 4 green, 3 red",
            "Game 3: 7 red, 7 blue, 9 green; 15 green, 4 red, 8 blue; 3 green, 12 blue, 6 red",
            "Game 4: 4 blue, 11 green, 6 red; 4 green, 2 red; 12 red, 1 blue, 3 green",
            "Game 5: 10 green, 4 blue, 9 red; 3 green, 15 blue, 11 red; 15 blue, 1 green, 2 red; 8 red, 8 blue, 5 green",
            "Game 6: 5 green, 19 red; 6 green, 13 red, 2 blue; 2 blue, 16 red, 4 green; 13 red, 9 blue, 5 green",
            "Game 7: 1 blue, 6 red, 6 green; 7 blue, 4 red; 6 green, 1 red, 11 blue; 3 green, 4 blue, 4 red; 6 green, 13 blue, 11 red",
            "Game 8: 8 green, 2 blue; 20 green, 1 red; 1 blue, 6 red, 6 green; 9 green",
            "Game 9: 5 red; 4 green, 3 red, 1 blue; 1 blue; 6 red, 1 blue, 9 green",
            "Game 10: 2 green, 3 red; 18 blue, 20 green, 9 red; 7 red, 9 blue, 17 green",
        ],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ),
)
def test_game_from_str(game: str, expected: int) -> None:
    assert Game.from_str(game).game_id == expected


@pytest.mark.parametrize(
    "games, expected",
    [
        (
            [
                "Game 37: 4 blue, 2 red, 8 green; 1 blue, 9 green, 4 red; 1 red, 4 green, 1 blue; 16 green, 3 blue, 4 red",
                "Game 15: 10 red, 2 blue, 18 green; 17 green, 3 blue, 7 red; 18 blue, 8 red, 12 green; 6 blue, 6 green, 12 red",
                "Game 20: 11 green; 1 blue, 4 green, 7 red; 7 green; 3 red, 1 blue, 6 green",
                "Game 16: 14 blue, 5 green, 12 red; 7 green, 3 red, 9 blue; 4 green, 1 red, 8 blue; 9 red, 19 green, 12 blue; 12 blue, 7 red, 6 green; 5 blue, 3 green, 6 red",
                "Game 87: 14 red, 4 blue, 4 green; 14 red, 4 blue, 7 green; 12 red, 11 green, 5 blue; 5 blue, 12 red",
                "Game 47: 1 green, 17 blue; 9 blue, 1 green; 1 blue, 1 red",
                "Game 13: 14 green, 1 red; 4 green; 2 green, 1 blue; 14 green; 13 green, 1 red, 1 blue; 1 blue, 1 red, 5 green",
                "Game 58: 9 red, 5 green; 10 green, 11 red, 1 blue; 12 green, 17 red, 1 blue; 1 blue, 1 green, 17 red; 14 red, 1 blue, 16 green",
                "Game 70: 10 green, 12 red; 5 red, 7 green; 1 blue, 6 red, 11 green",
                "Game 26: 3 blue, 5 red, 10 green; 7 green, 6 red; 7 green, 1 red, 3 blue; 10 green, 4 red, 3 blue; 4 red, 7 green, 3 blue; 8 green, 4 red",
            ],
            116,
        ),
        (
            [
                "Game 31: 8 red, 16 blue; 2 red, 1 green, 1 blue; 5 red, 8 blue, 1 green",
                "Game 87: 14 red, 4 blue, 4 green; 14 red, 4 blue, 7 green; 12 red, 11 green, 5 blue; 5 blue, 12 red",
                "Game 68: 3 blue, 10 red; 13 red, 1 green; 5 blue, 5 red; 2 blue, 1 green, 16 red; 16 red, 3 blue",
                "Game 54: 7 green, 16 blue, 5 red; 5 green; 10 blue, 6 green, 5 red; 3 green",
                "Game 94: 5 red, 1 green, 15 blue; 1 blue, 6 red; 2 red, 6 blue, 2 green",
                "Game 95: 9 blue, 4 red, 17 green; 15 green, 9 red, 10 blue; 1 blue, 13 green, 12 red",
                "Game 71: 16 green, 13 red, 10 blue; 7 red, 7 blue, 15 green; 17 green, 13 red, 1 blue; 5 blue, 8 green, 11 red; 7 red, 1 blue, 15 green; 15 green, 4 blue, 2 red",
                "Game 23: 5 green, 8 red, 1 blue; 2 red, 5 blue, 3 green; 2 green, 17 blue, 4 red; 2 blue, 2 red; 7 red, 1 green, 14 blue; 4 red, 8 blue",
                "Game 37: 4 blue, 2 red, 8 green; 1 blue, 9 green, 4 red; 1 red, 4 green, 1 blue; 16 green, 3 blue, 4 red",
                "Game 57: 14 blue, 2 red, 3 green; 1 red, 8 blue, 7 green; 1 green, 3 red, 15 blue; 5 green, 12 blue; 4 green, 15 blue",
            ],
            0,
        ),
        (
            [
                "Game 23: 5 green, 8 red, 1 blue; 2 red, 5 blue, 3 green; 2 green, 17 blue, 4 red; 2 blue, 2 red; 7 red, 1 green, 14 blue; 4 red, 8 blue",
                "Game 53: 5 green, 3 blue, 5 red; 2 red, 4 blue, 1 green; 1 red, 2 green; 11 red",
                "Game 94: 5 red, 1 green, 15 blue; 1 blue, 6 red; 2 red, 6 blue, 2 green",
                "Game 55: 3 green; 16 green, 1 blue; 13 green, 19 blue, 1 red; 13 green, 18 blue",
                "Game 41: 7 red, 4 blue, 4 green; 10 red, 11 blue, 1 green; 6 red, 6 blue, 4 green; 13 blue, 3 red, 7 green; 9 green, 12 blue, 14 red; 9 blue, 12 red, 10 green",
                "Game 7: 1 blue, 6 red, 6 green; 7 blue, 4 red; 6 green, 1 red, 11 blue; 3 green, 4 blue, 4 red; 6 green, 13 blue, 11 red",
                "Game 85: 1 red, 2 blue, 9 green; 13 green, 3 blue, 5 red; 1 green, 1 red, 3 blue; 8 green, 2 blue, 1 red",
                "Game 37: 4 blue, 2 red, 8 green; 1 blue, 9 green, 4 red; 1 red, 4 green, 1 blue; 16 green, 3 blue, 4 red",
                "Game 34: 4 green, 7 blue; 2 blue, 12 green; 6 red, 14 green, 7 blue",
                "Game 63: 7 red, 6 blue, 4 green; 2 blue, 5 green, 8 red; 5 blue, 4 green, 10 red; 4 blue, 7 red, 10 green; 5 blue, 10 green, 8 red; 4 blue, 10 green, 3 red",
            ],
            208,
        ),
    ],
)
def test_part_a(games: typing.List[str], expected: int) -> None:
    assert part_a([Game.from_str(game) for game in games]) == expected


@pytest.mark.parametrize(
    "games, expected",
    [
        (
            [
                "Game 62: 1 red, 1 blue, 2 green; 3 red, 1 blue, 2 green; 1 blue, 10 red; 6 red, 1 blue",
                "Game 92: 7 blue, 10 green; 9 green, 9 blue, 7 red; 6 green; 12 red, 1 blue, 4 green; 5 red, 1 green, 13 blue",
                "Game 64: 6 red, 7 green, 15 blue; 8 blue, 16 green, 3 red; 11 green, 12 blue; 4 red, 17 blue, 8 green",
                "Game 30: 8 blue, 3 red, 9 green; 10 green, 9 blue; 9 green, 12 blue; 3 blue, 2 red, 4 green; 8 blue, 9 green; 1 red, 12 blue, 6 green",
                "Game 3: 7 red, 7 blue, 9 green; 15 green, 4 red, 8 blue; 3 green, 12 blue, 6 red",
                "Game 77: 13 blue, 11 red, 1 green; 3 red, 12 green, 12 blue; 7 red, 15 green, 4 blue; 5 red, 2 green, 3 blue",
                "Game 99: 4 green, 2 blue, 4 red; 9 blue, 11 red, 1 green; 5 green",
                "Game 57: 14 blue, 2 red, 3 green; 1 red, 8 blue, 7 green; 1 green, 3 red, 15 blue; 5 green, 12 blue; 4 green, 15 blue",
                "Game 42: 3 blue, 1 red, 11 green; 4 blue, 9 green, 8 red; 3 red, 5 blue, 1 green",
                "Game 74: 6 green, 17 blue; 1 red, 1 blue, 11 green; 2 blue, 1 red, 3 green",
            ],
            8414,
        ),
        (
            [
                "Game 88: 3 green, 4 blue, 11 red; 3 green, 4 blue, 3 red; 10 red, 3 green; 3 blue, 2 red, 2 green",
                "Game 75: 11 red, 11 green, 3 blue; 11 red, 1 blue, 6 green; 4 green, 3 blue, 8 red",
                "Game 34: 4 green, 7 blue; 2 blue, 12 green; 6 red, 14 green, 7 blue",
                "Game 28: 5 green, 5 red, 2 blue; 1 blue, 9 red, 6 green; 2 blue, 3 red; 1 blue, 1 green, 5 red; 4 green, 3 red; 9 green, 1 blue, 14 red",
                "Game 35: 9 blue, 1 green; 2 green, 6 blue, 11 red; 1 green, 10 red, 1 blue",
                "Game 18: 12 red, 7 green, 7 blue; 3 blue, 8 red, 1 green; 2 green, 17 red",
                "Game 84: 8 blue, 1 green, 20 red; 9 green, 20 red, 18 blue; 16 red, 15 blue, 5 green; 15 red, 10 green, 16 blue; 11 green, 14 red, 12 blue",
                "Game 12: 3 green, 1 red, 8 blue; 9 blue, 3 red, 3 green; 4 blue, 1 green; 2 red, 3 green, 1 blue; 4 red, 7 blue, 3 green",
                "Game 16: 14 blue, 5 green, 12 red; 7 green, 3 red, 9 blue; 4 green, 1 red, 8 blue; 9 red, 19 green, 12 blue; 12 blue, 7 red, 6 green; 5 blue, 3 green, 6 red",
                "Game 20: 11 green; 1 blue, 4 green, 7 red; 7 green; 3 red, 1 blue, 6 green",
            ],
            9703,
        ),
        (
            [
                "Game 45: 9 green, 1 blue; 1 red, 5 green, 2 blue; 2 blue, 4 green, 9 red; 13 green, 7 red, 1 blue; 3 blue, 4 green",
                "Game 44: 2 red, 3 green, 5 blue; 5 red, 5 blue, 7 green; 2 red, 5 blue, 5 green; 6 red, 5 blue, 2 green",
                "Game 28: 5 green, 5 red, 2 blue; 1 blue, 9 red, 6 green; 2 blue, 3 red; 1 blue, 1 green, 5 red; 4 green, 3 red; 9 green, 1 blue, 14 red",
                "Game 11: 15 green, 7 blue, 9 red; 7 blue, 10 green, 7 red; 5 red, 3 blue, 10 green; 5 blue, 12 green; 14 green, 8 blue, 5 red; 7 blue, 2 red, 5 green",
                "Game 35: 9 blue, 1 green; 2 green, 6 blue, 11 red; 1 green, 10 red, 1 blue",
                "Game 83: 7 blue, 13 red; 4 blue, 2 green, 3 red; 15 blue, 9 red, 1 green; 14 red, 1 green, 12 blue",
                "Game 71: 16 green, 13 red, 10 blue; 7 red, 7 blue, 15 green; 17 green, 13 red, 1 blue; 5 blue, 8 green, 11 red; 7 red, 1 blue, 15 green; 15 green, 4 blue, 2 red",
                "Game 13: 14 green, 1 red; 4 green; 2 green, 1 blue; 14 green; 13 green, 1 red, 1 blue; 1 blue, 1 red, 5 green",
                "Game 25: 6 blue, 5 red, 10 green; 9 red, 3 blue, 3 green; 6 blue, 11 red, 15 green; 7 green, 10 red, 4 blue; 2 red, 20 blue, 11 green",
                "Game 56: 9 green; 3 blue, 1 red, 10 green; 1 red, 4 blue, 9 green",
            ],
            8075,
        ),
    ],
)
def test_part_b(games: typing.List[str], expected: int) -> None:
    assert part_b([Game.from_str(game) for game in games]) == expected
