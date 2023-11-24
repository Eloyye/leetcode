import heapq
from typing import List


class Solution:

    def minCostConnectPoints2(self, points: List[List[int]]) -> int:
        def calculate_distance(pt1, pt2):
            return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])
        def construct_adj_list(points):
            N = len(points)
            res = {i : [] for i in range(N)}
            for i in range(N):
                for j in range(i + 1, N):
                    dist = calculate_distance(points[i], points[j])
                    res[i].append(dist)
                    res[j].append(dist)
            return res

        def calculate_mst(adj_list, N):
            res = 0
            visit = set()
            min_heap = [(0, 0)]
            while len(visit) < N:
                cost, current_node = heapq.heappop(min_heap)
                if current_node in visit:
                    continue
                res += cost
                visit.add(current_node)
                for neighbor_cost, neighbor_node in adj_list[current_node]:
                    if neighbor_node not in visit:
                        heapq.heappush(min_heap, (neighbor_cost, neighbor_node))
            return res


        return calculate_mst(construct_adj_list(points), len(points))
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def create_adjancency_list(pts: List[List[int]]) -> dict[int : list[tuple[int, int]]]:
            N = len(pts)
            res = {i : [] for i in range(N)}
            for i in range(N):
                x1, y1 = pts[i]
                for j in range(i + 1, N):
                    x2, y2 = pts[j]
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    # MST is bidirectional
                    # (dist, outgoing node), dist first b/c of minHeap
                    res[i].append((distance, j))
                    res[j].append((distance, i))
            return res
        adj = create_adjancency_list(points)

        def calculate_mst(adj : dict[int : list[tuple[int, int]]], N : int) -> int:
            res = 0
            visit = set()
            minH = [(0, 0)]
            while len(visit) < N:
                cost, i = heapq.heappop(minH)
                if i in visit:
                    continue
                res += cost
                visit.add(i)
                for neighbor_cost, neighbor_node in adj[i]:
                    if neighbor_node not in visit:
                        heapq.heappush(minH, (neighbor_cost, neighbor_node))
            return res


        return calculate_mst(adj, len(points))
