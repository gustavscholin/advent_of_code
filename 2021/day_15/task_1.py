import numpy as np

from utils.read_input import read_input_as_matrix
from utils.graphs import shortest_path


if __name__ == "__main__":
    risk_map = read_input_as_matrix("2021/day_15/input.txt", "int")
    vertices = []
    edges = {}
    for i in range(len(risk_map)):
        for j in range(len(risk_map[i])):
            vertice = (i, j)
            vertices.append(vertice)
            neighbour_edges = {}
            for offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neighbour = np.add(vertice, offset)
                if np.all(np.logical_and(neighbour >= 0, neighbour < len(risk_map))):
                    neighbour_edges[tuple(neighbour)] = risk_map[neighbour[0]][
                        neighbour[1]
                    ]
            edges[vertice] = neighbour_edges

    start = (0, 0)
    destination = (len(risk_map) - 1, len(risk_map) - 1)
    print(shortest_path(vertices, edges, start, destination))
