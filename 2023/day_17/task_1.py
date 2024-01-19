import heapq as hq
from collections import defaultdict

import numpy as np

from utils.read_input import read_input_as_matrix


def is_valid_step(current_vertex, next_vertex, paths):
    if (
        paths[current_vertex]
        and paths[paths[current_vertex]]
        and paths[paths[paths[current_vertex]]]
    ):
        three_steps_back = paths[paths[paths[current_vertex]]][0]
    else:
        three_steps_back = (0, 0)
    one_step_back = paths[current_vertex][0]
    return one_step_back != next_vertex[0] and not (
        (
            three_steps_back[0] == next_vertex[0][0]
            and abs(three_steps_back[1] - next_vertex[0][1]) == 4
        )
        or (
            three_steps_back[1] == next_vertex[0][1]
            and abs(three_steps_back[0] - next_vertex[0][0]) == 4
        )
    )


def shortest_path(
    vertices: list[tuple[int]],
    edges: dict[tuple[int], dict[tuple[int], int]],
    start: tuple[int],
    destination: tuple[int],
):
    """An implementation of Dijkstra's shortest path algorithm"""
    visited = {v: False for v in vertices}
    visited = set()
    distances = {v: float("inf") for v in vertices}
    distances = defaultdict(lambda: float("inf"))
    paths = {v: None for v in vertices}
    paths = defaultdict(lambda: ((0, 0), None))
    queue = []
    distances[start] = 0
    hq.heappush(queue, (0, start, None))
    while queue:
        g, u, dir = hq.heappop(queue)
        visited.add((u, dir))
        if u == destination:
            return paths, distances
        for v, w in edges[u].items():
            v_dir = (v[0] - u[0], v[1] - u[1])
            if not (v, v_dir) in visited and is_valid_step((u, dir), (v, v_dir), paths):
                f = g + w
                if f < distances[(v, v_dir)]:
                    distances[(v, v_dir)] = f
                    paths[(v, v_dir)] = (u, dir)
                    hq.heappush(queue, (f, v, v_dir))
    return paths, distances


if __name__ == "__main__":
    risk_map = read_input_as_matrix("2023/day_17/sample_input.txt", "int")
    vertices = []
    edges = {}
    for i in range(len(risk_map)):
        for j in range(len(risk_map[i])):
            vertex = (i, j)
            vertices.append(vertex)
            neighbor_edges = {}
            for offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neighbor = np.add(vertex, offset)
                if np.all(np.logical_and(neighbor >= 0, neighbor < len(risk_map))):
                    neighbor_edges[tuple(neighbor)] = risk_map[neighbor[0]][neighbor[1]]
            edges[vertex] = neighbor_edges

    start = (0, 0)
    destination = (len(risk_map) - 1, len(risk_map) - 1)
    paths, dist = shortest_path(vertices, edges, start, destination)
    print()
    v = destination
    while v[0] != (0, 0):
        print(v)
        v = paths[v]
    pass
