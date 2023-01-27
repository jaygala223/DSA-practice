class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        costs = [1e9]*(n+1)
        costs[src] = 0
        
        for i in range(k+1):
            cost = costs.copy()
            for u, v, w in flights:
                if costs[u] + w < cost[v]:
                    cost[v] = costs[u] + w
            costs = cost
        
        return costs[dst] if costs[dst] != 1e9 else -1
                