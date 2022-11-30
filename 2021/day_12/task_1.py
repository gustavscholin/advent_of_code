from copy import deepcopy
from collections import defaultdict
from utils.read_input import read_input


def find_paths(start, path):
    path.append(start)
    if start == "end":
        paths.append(path)
        return
    for node in graph[start]:
        if node.islower() and node in path:
            continue
        find_paths(node, deepcopy(path))


if __name__ == "__main__":
    connections = read_input("day_12/input.txt")
    graph = defaultdict(list)

    for connection in connections:
        node_1, node_2 = connection.split("-")
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    paths = []
    find_paths("start", [])
    print(len(paths))
