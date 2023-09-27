from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self,
                          n: int,
                          flights: List[List[int]],
                          src: int,
                          dst: int,
                          k: int) -> int:
        reach_cost = [float("infinity")] * n
        reach_cost[src] = 0

        for _ in range(k + 1):
            precommit_cost = reach_cost.copy()

            for source_node, destination_node, edge_price in flights:
                if reach_cost[source_node] == float('infinity'):
                    continue
                if reach_cost[source_node] + edge_price < precommit_cost[destination_node]:
                    precommit_cost[destination_node] = reach_cost[source_node] + edge_price
            reach_cost = precommit_cost
        res = reach_cost[dst]
        return res if res != float('infinity') else -1