import dataclasses
import math
import typing

import networkx as nx


@dataclasses.dataclass
class Component:
    name: str
    connected: typing.List[str]

    @classmethod
    def from_str(cls, line: str) -> "Component":
        name, connected = line.split(": ")
        return cls(name, connected.split(" "))


def get_input(file_name: str) -> typing.List[Component]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return [Component.from_str(line) for line in lines]


def part_a(components: typing.List[Component]) -> int:
    graph = nx.Graph()
    graph.add_nodes_from([component.name for component in components])
    for component in components:
        for connected in component.connected:
            graph.add_edge(component.name, connected)
    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    return math.prod(len(component) for component in nx.connected_components(graph))


def part_b(components: typing.List[Component]) -> int:
    return 0


if __name__ == "__main__":
    print(part_a(get_input("../bin/25.txt")))
