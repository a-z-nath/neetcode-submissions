class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        l1, l2 = len(s1), len(s2)
        dp = {}
        def dfs(i, j):
            if i + j == len(s3):
                return True
            if i >= l1 and j >= l2:
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            flag = False
            if i < l1 and s1[i] == s3[i+j]:
                flag |= dfs(i+1, j)
            if j < l2 and s2[j] == s3[i+j]:
                flag |= dfs(i, j+1)
            dp[(i, j)] = flag
            return dp[(i, j)]
        return dfs(0, 0)