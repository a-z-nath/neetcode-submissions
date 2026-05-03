class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        rows, cols = len(grid), len(grid[0])
        neghbours = [[-1, 0],[1, 0],[0,-1],[0, 1]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append(([i, j], 0))
        print(queue)
        while len(queue) != 0:
            pos, dist = queue.pop(0)
            r, c = pos
            for nc in neghbours:
                i, j = r + nc[0], c + nc[1]
                if 0 <= i < rows  and 0 <= j < cols and 1 + dist < grid[i][j]:
                    grid[i][j] = 1 + dist
                    queue.append(([i, j], 1 + dist))
        return