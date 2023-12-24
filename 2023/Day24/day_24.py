import dataclasses
import typing

from z3 import Int, Solver, sat

LOWER_BOUND = 200000000000000
UPPER_BOUND = 400000000000000


@dataclasses.dataclass
class HailStone:
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int

    def intersection(self, other: "HailStone") -> typing.Optional[typing.Tuple[float, float]]:
        x1, x2, x3, x4 = self.x, self.x + self.vx, other.x, other.x + other.vx
        y1, y2, y3, y4 = self.y, self.y + self.vy, other.y, other.y + other.vy

        det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if det != 0:
            px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
            py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det
            valid_a = (px > x1) == (x2 > x1)
            valid_b = (px > x3) == (x4 > x3)

            if LOWER_BOUND <= px <= UPPER_BOUND and LOWER_BOUND <= py <= UPPER_BOUND and valid_a and valid_b:
                return (px, py)

        return None

    @classmethod
    def from_str(cls, line: str) -> "HailStone":
        pos, vel = line.split(" @ ")
        x, y, z = map(int, pos.split(", "))
        vx, vy, vz = map(int, vel.split(", "))
        return cls(x, y, z, vx, vy, vz)


def get_input(file_name: str) -> typing.List[HailStone]:
    with open(file_name, "r") as f:
        lines = f.read().splitlines()
    return [HailStone.from_str(line) for line in lines]


def part_a(lines: typing.List[HailStone]) -> int:
    intersections = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            pos = lines[i].intersection(lines[j])
            if pos is not None:
                intersections.append(pos)
    return len(intersections)


def part_b(lines: typing.List[HailStone]) -> int:
    solver = Solver()
    x, y, z = Int("x"), Int("y"), Int("z")
    vx, vy, vz = Int("vx"), Int("vy"), Int("vz")
    t = [Int(f"t{i}") for i in range(len(lines))]
    for i, line in enumerate(lines):
        solver.add(x + t[i] * vx - line.x - t[i] * line.vx == 0)
        solver.add(y + t[i] * vy - line.y - t[i] * line.vy == 0)
        solver.add(z + t[i] * vz - line.z - t[i] * line.vz == 0)
    if solver.check() != sat:
        raise ValueError("No solution found")
    model = solver.model()
    return int(model.eval(x + y + z).as_long())


if __name__ == "__main__":
    print(part_a(get_input("../bin/24.txt")))
    print(part_b(get_input("../bin/24.txt")))
