class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        def findPaths(i: int, j: int):
            # out of board
            if i < 0 or i >= m:
                return 0
            if j < 0 or j >= n:
                return 0
            # start
            if i == 0 and j == 0:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            
            rightPath = findPaths(i, j-1)
            downPath = findPaths(i-1, j)
            dp[i][j] = rightPath + downPath
            return dp[i][j]
        return findPaths(m-1, n-1)