import typing
from itertools import groupby


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def lowest_location(
    seed_ranges: typing.List[typing.Tuple[typing.List[typing.List[typing.Tuple[int, ...]]], int, int]]
) -> float:
    lowest = float("inf")
    while seed_ranges:
        range_conversions, lo, hi = seed_ranges.pop()
        try:
            conversion, *remaining_conversions = range_conversions
        except ValueError:
            lowest = min(lowest, lo)
            continue

        for dest, source_lowest, length in conversion:
            source_highest = source_lowest + length - 1
            if lo <= source_highest and source_lowest < hi:
                seed_ranges.append(
                    (
                        remaining_conversions,
                        range(dest, dest + length)[
                            range(source_lowest, source_lowest + length).index(max(lo, source_lowest))
                        ],
                        range(dest, dest + length)[
                            range(source_lowest, source_lowest + length).index(min(hi, source_highest))
                        ],
                    )
                )

                if lo < source_lowest:
                    seed_ranges.append((remaining_conversions, lo, source_lowest))

                lo = source_lowest + length
                if lo >= hi:
                    break
        else:
            seed_ranges.append((remaining_conversions, lo, hi))

    return lowest


def part_a(lines: typing.List[str]) -> float:
    seeds, *blocks = [tuple(group) for has_content, group in groupby(lines, bool) if has_content]
    conversions = [sorted((tuple(map(int, y.split())) for y in x[1:]), key=lambda x: x[1]) for x in blocks]
    return lowest_location([(conversions, int(seed), int(seed) + 1) for seed in seeds[0].split()[1:]])


def part_b(lines: typing.List[str]) -> float:
    seeds, *blocks = [tuple(group) for has_content, group in groupby(lines, bool) if has_content]
    seeds = tuple(map(int, seeds[0].split()[1:]))  # type: ignore
    conversions = [sorted((tuple(map(int, y.split())) for y in x[1:]), key=lambda x: x[1]) for x in blocks]
    return lowest_location([(conversions, lo, lo + range_length) for lo, range_length in zip(*2 * [iter(seeds)])])


if __name__ == "__main__":
    print(part_a(get_input("../bin/5.txt")))
    print(part_b(get_input("../bin/5.txt")))
