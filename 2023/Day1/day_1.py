import typing

NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def get_integer(text: str, *, parse_words: bool = False) -> int:
    pos_map = {n: j for n, j in enumerate(text) if j.isdigit()}
    if parse_words:
        pos_map |= {n: v for n in range(len(text)) for k, v in NUMBERS.items() if k == text[n : n + len(k)]}
    return int(pos_map[min(pos_map.keys())] + pos_map[max(pos_map.keys())])


def part_a(lines: typing.List[str]) -> int:
    return sum(get_integer(i) for i in lines)


def part_b(lines: typing.List[str]) -> int:
    return sum(get_integer(i, parse_words=True) for i in lines)


if __name__ == "__main__":
    print(part_a(get_input("../bin/1.txt")))
    print(part_b(get_input("../bin/1.txt")))
