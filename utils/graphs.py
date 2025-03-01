import heapq as hq


def shortest_path(
    vertices: list[tuple[int]],
    edges: dict[tuple[int], dict[tuple[int], int]],
    start: tuple[int],
    destination: tuple[int],
):
    """An implementation of Dijkstra's shortest path algorithm"""
    visited = {v: False for v in vertices}
    distances = {v: float("inf") for v in vertices}
    paths = {v: None for v in vertices}
    queue = []
    distances[start] = 0
    hq.heappush(queue, (0, start))
    while queue:
        g, u = hq.heappop(queue)
        visited[u] = True
        if u == destination:
            return distances[destination]
        for v, w in edges[u].items():
            if not visited[v]:
                f = g + w
                if f < distances[v]:
                    distances[v] = f
                    paths[v] = u
                    hq.heappush(queue, (f, v))
    return paths, distances


def all_shortest_paths(
    vertices: list[tuple[int]],
    edges: dict[tuple[int], dict[tuple[int], int]],
    start: tuple[int],
    destination: tuple[int],
):
    """An implementation of Dijkstra's all shortest paths algorithm"""
    visited = {v: False for v in vertices}
    distances = {v: float("inf") for v in vertices}
    paths = {v: set() for v in vertices}
    queue = []
    distances[start] = 0
    hq.heappush(queue, (0, start))
    while queue:
        g, u = hq.heappop(queue)
        visited[u] = True
        if u == destination:
            return paths, distances[destination]
        if edges.get(u):
            for v, w in edges[u].items():
                if not visited[v]:
                    f = g + w
                    if f < distances[v]:
                        distances[v] = f
                        paths[v].clear()
                        paths[v].add(u)
                        hq.heappush(queue, (f, v))
                    elif f == distances[v]:
                        paths[v].add(u)
    return paths, distances
