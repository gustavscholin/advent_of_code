import re

from collections import defaultdict
from itertools import combinations
from copy import deepcopy
from utils.read_input import read_input
from utils.graphs import shortest_path


def search(curr_vertex: str, opened: list, min_left, curr_flow, sum_flow):
    global best_flow
    if curr_vertex not in opened:
        min_left -= 1
        sum_flow += curr_flow
        opened.append(curr_vertex)
        curr_flow += rates[curr_vertex]
    flow = sum_flow + curr_flow * min_left
    if flow > best_flow:
        best_flow = flow
    for neighbor, travel_time in edges_reduced[curr_vertex].items():
        if neighbor not in opened and min_left - travel_time >= 3:
            search(
                neighbor,
                deepcopy(opened),
                min_left - travel_time,
                curr_flow,
                sum_flow + curr_flow * travel_time,
            )


if __name__ == "__main__":
    report = read_input("2022/day_16/input.txt")
    vertices_complete = []
    edges_complete = {}
    rates = {}

    for row in report:
        vertices = re.findall(r"[A-Z]{2}", row)
        rate = int(re.findall(r"\d+", row)[0])
        vertex = vertices[0]

        rates[vertex] = rate
        vertices_complete.append(vertex)
        edges_complete[vertex] = {}
        for v in vertices[1:]:
            edges_complete[vertex][v] = 1

    vertices_reduced = [v for v in vertices_complete if rates[v] > 0] + ["AA"]
    edges_reduced = defaultdict(dict)
    for v1, v2 in combinations(vertices_reduced, 2):
        dist = shortest_path(vertices_complete, edges_complete, v1, v2)
        edges_reduced[v1][v2] = dist
        edges_reduced[v2][v1] = dist

    best_flow = 0
    search("AA", ["AA"], 30, 0, 0)
    print(best_flow)
