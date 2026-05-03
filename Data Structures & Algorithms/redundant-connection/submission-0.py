class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        def has_path(v, target, visited):
            if v == target:
                return True
            visited.add(v)
            for nh in adj[v]:
                if nh not in visited:
                    if has_path(nh, target, visited):
                        return True
            return False

        for v1, v2 in edges:
            if v1 in adj and v2 in adj and has_path(v1, v2, set()):
                return [v1, v2]
            adj[v1].append(v2)
            adj[v2].append(v1)
        return [-1, -1]