import re

from ortools.constraint_solver import pywrapcp

from utils.read_input import read_input

if __name__ == "__main__":
    lines = read_input("2022/day_15/input.txt")
    solver = pywrapcp.Solver("CPSimple")
    max_pos = 4_000_000
    min_pos = 0

    x = solver.IntVar(min_pos, max_pos, "x")
    y = solver.IntVar(min_pos, max_pos, "y")
    for l in lines:
        s_x, s_y, b_x, b_y = map(int, re.findall(r"-?\d+", l))
        dist = abs(s_x - b_x) + abs(s_y - b_y)
        solver.Add(abs(s_x - x) + abs(s_y - y) > dist)

    decision_builder = solver.Phase(
        [x, y], solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE
    )

    solver.NewSearch(decision_builder)
    solver.NextSolution()
    print(x.Value() * 4_000_000 + y.Value())
