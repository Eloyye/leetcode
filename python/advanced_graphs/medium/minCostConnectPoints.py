import heapq
from typing import List


class Solution:

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
