class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(i: int, j: int):
            if not (0 <= i < rows) or not (0 <= j < cols):
                return 0
            if grid[i][j] != 1 or (i, j) in visited:
                return 0
            visited.add((i, j))
            area = dfs(i - 1, j)
            area += dfs(i + 1, j)
            area += dfs(i, j - 1)
            area += dfs(i, j + 1)
            return area + 1
        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(dfs(r, c), area)
        return area