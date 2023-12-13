import heapq as hq

import numpy as np

from utils.graphs import shortest_path
from utils.read_input import read_input_as_matrix


def get_height(i, j):
    if height_map[i][j] == "S":
        return "a"
    elif height_map[i][j] == "E":
        return "z"
    return height_map[i][j]


if __name__ == "__main__":
    height_map = read_input_as_matrix("2022/day_12/input.txt")
    vertices = []
    edges = {}
    starts = []
    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            if get_height(i, j) == "a":
                starts.append((i, j))
            elif height_map[i][j] == "E":
                destination = (i, j)
            height = get_height(i, j)
            vertex = (i, j)
            vertices.append(vertex)
            neighbor_edges = {}
            for offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neighbor = np.add(vertex, offset)
                if (
                    np.all(
                        np.logical_and(
                            neighbor >= 0,
                            neighbor < np.array([len(height_map), len(height_map[i])]),
                        )
                    )
                    and ord(get_height(neighbor[0], neighbor[1])) - ord(height) <= 1
                ):
                    neighbor_edges[tuple(neighbor)] = 1
            edges[vertex] = neighbor_edges

    paths = []
    for start in starts:
        path = shortest_path(vertices, edges, start, destination)
        if type(path) == int:
            paths.append(path)
    print(min(paths))
