class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        totalcost = 0
        n = len(points)
        visited = [False] * n
        pq = [(0, 0)] # (cost, vertex)
        while pq:
            cost, i = heapq.heappop(pq)
            if visited[i]:
                continue
            visited[i] = True
            totalcost += cost
            for j in range(n):
                if not visited[j]:
                    heapq.heappush(pq, (manhattan_dist(i,j), j))
        return totalcost