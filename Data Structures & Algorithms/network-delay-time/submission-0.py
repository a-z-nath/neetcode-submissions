class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append([v, t]) # [u] => [[v1, t1], [v2, t2]]
        dist = defaultdict(int)
        dist[k] = 0
        pq = [[k, 0]] # [vertex, min_time]
        heapq.heapify(pq)
        while len(pq) != 0:
            u, t = heapq.heappop(pq)
            for v, t1 in adj[u]:
                if (v in dist and t + t1 < dist[v]) or v not in dist:
                    heapq.heappush(pq, [v, t + t1])
                    dist[v] = t + t1
        if len(dist) != n:
            return -1
        return max(dist.values())