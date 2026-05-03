class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # topological sort problem with bi-direction
        if len(edges) != n - 1:
            return False
        adj_list = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for ch in adj_list[node]:
                if ch == parent:
                    continue
                if not dfs(ch, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visited) == n