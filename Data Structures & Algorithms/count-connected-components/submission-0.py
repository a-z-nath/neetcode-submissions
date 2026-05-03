class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        visited = set()
        def dfs(v):
            if v in visited:
                return 0
            visited.add(v)
            for n in adj[v]:
                if n in visited:
                    continue
                dfs(n)
            return 1
        trees = 0
        for i in range(n):
            trees += dfs(i)
        return trees