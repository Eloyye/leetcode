import heapq
from collections import defaultdict
from typing import List




class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def constructAdjacencyList(times, n):
            edges = defaultdict(list)
            for outgoing_node, incoming_node, distance in times:
                edges[outgoing_node].append((distance, incoming_node))
            return edges
        edges = constructAdjacencyList(times, n)
        min_heap = [(0, k)]
        visit = set()
        min_delay_time = 0
        while min_heap:
            distance_from_k_to_current, current_node = heapq.heappop(min_heap)
            if current_node in visit:
                continue
            visit.add(current_node)
            min_delay_time = max(min_delay_time, distance_from_k_to_current)
            for distance_from_current_to_neighbor, neighbor_node in edges[current_node]:
                if neighbor_node not in visit:
                    heapq.heappush(min_heap, (distance_from_k_to_current + distance_from_current_to_neighbor, neighbor_node))
        return min_delay_time if len(visit) == n else -1
