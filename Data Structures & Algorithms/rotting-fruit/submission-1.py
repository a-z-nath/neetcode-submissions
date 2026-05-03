class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        neighbors = [[-1, 0],[1, 0], [0, -1], [0, 1]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i, j])
        if fresh == 0:
            return 0
        while len(q) != 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nc in neighbors:
                    i, j = r + nc[0], c + nc[1]
                    if 0 <= i < rows and 0 <= j < cols and fresh > 0 and grid[i][j] == 1:
                        grid[i][j] = 2
                        q.append([i, j])
                        fresh -= 1
            time += 1

        return time-1 if fresh == 0 else -1