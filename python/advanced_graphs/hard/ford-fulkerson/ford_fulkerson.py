# graph: graph as 2d matrix representation
def ford_fulkerson(graph: list[list[int]], source: int, sink: int) -> int:
    # parent: parent array to store path from source to sink
    parent = [-1] * len(graph)
    max_flow = 0

    # Depth-first search to find path from source to sink
    def dfs(graph: list[list[int]], source: int, sink: int, parent: list[int]) -> bool:
        visited = [False] * len(graph)
        stack = [source]
        visited[source] = True
        while stack:
            u = stack.pop()
            for v, capacity in enumerate(graph[u]):
                if not visited[v] and capacity > 0:
                    stack.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    # Augment the flow while there is path from source to sink
    while dfs(graph, source, sink, parent):
        # path_flow: find minimum residual capacity of the edges along the path filled by dfs
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow


if __name__ == '__main__':
    # Example usage
    # Matrix representation of graph
    graph = [[0, 8, 0, 0, 3, 0],
             [0, 0, 9, 0, 0, 0],
             [0, 0, 0, 0, 7, 2],
             [0, 0, 0, 0, 0, 5],
             [0, 0, 7, 4, 0, 0],
             [0, 0, 0, 0, 0, 0]]

    source = 0  # Starting node
    sink = 5  # Ending node
    print("The maximum possible flow is", ford_fulkerson(graph, source, sink))
