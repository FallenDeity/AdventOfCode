import typing


def get_input(file_name: str) -> typing.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def extrapolate(nums: typing.List[int]) -> int:
    nn = [b - a for a, b in zip(nums, nums[1:])]
    return nums[-1] + extrapolate(nn) if any(nn) else nums[-1]


def part_a(lines: typing.List[str]) -> int:
    nums = [list(map(int, line.split())) for line in lines]
    return sum(extrapolate(num) for num in nums)


def part_b(lines: typing.List[str]) -> int:
    nums = [list(map(int, line.split())) for line in lines]
    return sum(extrapolate(num[::-1]) for num in nums)


if __name__ == "__main__":
    print(part_a(get_input("../bin/9.txt")))
    print(part_b(get_input("../bin/9.txt")))
