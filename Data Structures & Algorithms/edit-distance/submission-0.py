class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = {}

        def dfs(i: int, j: int):
            if i >= l1 and j >= l2:
                return 0
            if j == l2:
                return l1 - i
            if i == l1:
                return l2 - j
            if (i, j) in dp:
                return dp[(i, j)]
            
            step = float("inf")
            # match go diagonally
            if word1[i] == word2[j]:
                step = dfs(i+1, j+1)
            else:
                step = min(step, 1 + dfs(i + 1, j)) # delete
                step = min(step, 1 + dfs(i + 1, j + 1)) # replace
                step = min(step, 1 + dfs(i, j + 1)) # insert
            dp[(i, j)] = step
            return dp[(i, j)]
        return dfs(0, 0)