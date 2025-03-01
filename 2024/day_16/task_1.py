from utils.graphs import shortest_path
from utils.read_input import read_input_as_matrix


def get_neighbors(x, y):
    return [(x + dx, y + dy) for dx, dy in dirs]


if __name__ == "__main__":
    maze = read_input_as_matrix("2024/day_16/input.txt")
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    vertices = []
    edges = {}
    for i in range(1, len(maze) - 1):
        for j in range(1, len(maze[i]) - 1):
            point_type = maze[i][j]
            if point_type == "#":
                continue
            if point_type == "E":
                destination = (i, j)
                vertices.append((i, j))
            else:
                if point_type == "S":
                    start = (i, j, 1)
                for d in range(4):
                    vertices.append((i, j, d))
                    edges[(i, j, d)] = {
                        (i, j, (d - 1) % 4): 1000,
                        (i, j, (d + 1) % 4): 1000,
                    }

                for d, (ni, nj) in enumerate(get_neighbors(i, j)):
                    n_point_type = maze[ni][nj]
                    if n_point_type != "#":
                        if n_point_type == "E":
                            edges[(i, j, d)][(ni, nj)] = 1
                        else:
                            edges[(i, j, d)][(ni, nj, d)] = 1

    print(shortest_path(vertices, edges, start, destination))
