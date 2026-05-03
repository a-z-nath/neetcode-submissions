class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def commonSubsequence(i: int, j: int):
            # out bound
            if i < 0 or i >= m:
                return 0
            if j < 0 or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            subseq = 0
            if text1[i] == text2[j]:
                subseq = 1 + commonSubsequence(i-1, j-1)
            else:
                subseq1 = commonSubsequence(i-1, j)
                subseq2 = commonSubsequence(i, j-1)
                subseq = max(subseq1, subseq2)
            dp[i][j] = subseq
            return subseq
        return commonSubsequence(m-1, n-1)