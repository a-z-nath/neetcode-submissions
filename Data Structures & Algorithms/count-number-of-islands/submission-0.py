class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0, -1], [0, 1]]
        def dfs(i: int, j: int):
            if i < 0 or i >= rows:
                return 0
            if j < 0 or j >= cols:
                return 0
            if (i, j) in visited:
                return 0
            if grid[i][j] != "1":
                return
            visited.add((i, j))
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                dfs(ni, nj)
            return 1
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                        islands += dfs(r, c)
        return islands