import sys
import typing as t

sys.setrecursionlimit(100_000)


Graph = t.Dict[t.Tuple[int, int], t.Dict[t.Tuple[int, int], int]]
Point = t.Tuple[int, int]


def get_input(file_name: str) -> t.List[str]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return lines


def is_valid_move(grid: t.List[str], pos: Point, visited: t.List[t.List[bool]], direction: Point) -> bool:
    x, y = pos
    rows, cols = len(grid), len(grid[0])
    return (
        0 <= x < rows
        and 0 <= y < cols
        and grid[x][y] != "#"
        and not visited[x][y]
        and is_downhill(grid, x, y, direction)
    )


def is_downhill(grid: t.List[str], x: int, y: int, direction: t.Tuple[int, int]) -> bool:
    slope_map = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}
    return grid[x][y] == "." or slope_map[grid[x][y]] == direction


def dfs(grid: t.List[str], start: Point, end: Point, visited: t.List[t.List[bool]], current_length: int) -> int:
    x, y = start
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_length = current_length
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        if is_valid_move(grid, (new_x, new_y), visited, (dx, dy)):
            visited[new_x][new_y] = True
            next_length = dfs(grid, (new_x, new_y), end, visited, current_length + 1)
            max_length = max(max_length, next_length)
            visited[new_x][new_y] = False

    return max_length


def make_adjacencies(graph: t.List[str]) -> Graph:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = {
        (i, j): {
            (x, y): 1
            for dx, dy in directions
            for x, y in [(i + dx, j + dy)]
            if 0 <= x < len(graph) and 0 <= y < len(graph[0]) and graph[x][y] != "#"
        }
        for i, row in enumerate(graph)
        for j, c in enumerate(row)
        if c != "#"
    }
    for key in list(res.keys()):
        neighbors = res[key]
        if len(neighbors) == 2:
            left, right = neighbors.keys()
            res[left][right] = max(res[left].get(right, 0), neighbors[left] + neighbors[right])
            res[right][left] = res[left][right]
            del res[left][key]
            del res[right][key]
            del res[key]
    return res


def dfs_modified(graph: Graph, start: t.Tuple[int, int], end: t.Tuple[int, int]) -> int:
    stack = [(start, {start: 0})]
    best = None

    while stack:
        current, path = stack.pop()

        if current == end:
            current_sum = sum(path.values())
            best = max(best or current_sum, current_sum)
            continue

        for neighbor in graph[current]:
            if neighbor not in path:
                new_path = dict(path)
                new_path[neighbor] = graph[current][neighbor]
                stack.append((neighbor, new_path))

    return best or -1


def part_a(grid: t.List[str]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    end = len(grid) - 1, len(grid[0]) - 2
    return dfs(grid, (0, 1), end, visited, 0)


def part_b(grid: t.List[str]) -> int:
    graph = make_adjacencies(grid)
    end = len(grid) - 1, len(grid[0]) - 2
    return dfs_modified(graph, (0, 1), end)


if __name__ == "__main__":
    print(part_a(get_input("../bin/23.txt")))
    print(part_b(get_input("../bin/23.txt")))
