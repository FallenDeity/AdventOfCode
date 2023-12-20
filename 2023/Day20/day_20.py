from __future__ import annotations

from collections import deque
from itertools import count
from math import lcm
from typing import Callable, Literal


def parse_component(raw: str) -> tuple[str, Literal["%", "&", ""], list[str]]:
    name, params = raw.split(" -> ")
    mode: Literal["%", "&", ""] = ""
    match name[0]:
        case "%":
            mode = "%"
            name = name[1:]
        case "&":
            mode = "&"
            name = name[1:]
        case _:
            mode = ""
    return name, mode, params.split(", ")


def parse_raw(raw: str) -> dict[str, tuple[Literal["%", "&", ""], list[str]]]:
    modules = list(raw.splitlines())
    return {name: (mode, params) for name, mode, params in map(parse_component, modules)}


def get_input(file_name: str) -> dict[str, tuple[Literal["%", "&", ""], list[str]]]:
    with open(file_name, "r") as f:
        raw = f.read()
    return parse_raw(raw)


def handle(
    states: dict[str, bool],
    remembered: dict[str, dict[str, bool]],
    data: dict[str, tuple[Literal["%", "&", ""], list[str]]],
    on_activate: Callable[[str, bool, str], None] = lambda mod, pulse, origin: None,
) -> tuple[int, int]:
    modules = data["broadcaster"][1]
    queue = deque((mod, bool(), str("broadcaster")) for mod in modules)
    high, low = 0, 0
    while queue:
        name, pulse, origin = queue.popleft()
        on_activate(name, pulse, origin)
        high, low = (high + 1, low) if pulse else (high, low + 1)
        if name not in data:
            continue
        mode, params = data[name]
        match mode:
            case "%":
                if not pulse:
                    states[name] = not states[name]
                    queue.extend((mod, states[name], name) for mod in params)
            case "&":
                remembered[name][origin] = pulse
                pulse = not all(remembered[name].values())
                queue.extend((mod, pulse, name) for mod in params)
            case "":
                queue.extend((mod, pulse, name) for mod in params)
    return high, low


def part_a(data: dict[str, tuple[Literal["%", "&", ""], list[str]]]) -> int:
    states = {name: False for name, (mode, _) in data.items() if mode == "%"}
    remembered = {
        name: {input: False for input, (_, params) in data.items() if name in params}
        for name, (mode, _) in data.items()
        if mode == "&"
    }
    total_high, total_low = 0, 0
    for _ in range(1000):
        high, low = handle(states, remembered, data)
        total_high, total_low = total_high + high, total_low + low + 1

    return total_high * total_low


def part_b(data: dict[str, tuple[Literal["%", "&", ""], list[str]]]) -> int:
    states = {name: False for name, (mode, _) in data.items() if mode == "%"}
    remembered = {
        name: {input: False for input, (_, params) in data.items() if name in params}
        for name, (mode, _) in data.items()
        if mode == "&"
    }
    source = next(name for name, (_, params) in data.items() if "rx" in params)
    sources = list(remembered[source].keys())

    cycles = {}
    for i in count(1):

        def on_activate(mod: str, pulse: bool, _: str) -> None:
            if mod in sources and not pulse and mod not in cycles:
                cycles[mod] = i

        handle(states, remembered, data, on_activate)

        if len(cycles) == len(sources):
            return lcm(*cycles.values())

    return -1


if __name__ == "__main__":
    print(part_a(get_input("../bin/20.txt")))
    print(part_b(get_input("../bin/20.txt")))
