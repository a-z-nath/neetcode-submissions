class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, w in flights:
            adj[u].append([v, w])
        costs = [float("inf")] * (n + 1)
        pq = [(0, src, 0)] # (cost, airport, stopage)
        costs[src] = 0
        while pq:
            c, airport, stop = heapq.heappop(pq)
            if airport == dst:
                return c
            if stop > k:
                continue
            for v, cost in adj[airport]:
                heapq.heappush(pq, (c+ cost, v, stop + 1))
        return -1