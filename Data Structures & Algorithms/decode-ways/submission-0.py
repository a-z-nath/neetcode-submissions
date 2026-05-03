class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1 for _ in range(len(s))]
        def decoding(s: str, i: int)-> int:
            n = len(s)
            if i == n:
                return 1
            elif s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]
            
            # recurring relation 
            # take 1 char cur or take 2 char starting at cur
            # all valid paths are total decoding count
            pathcnt = decoding(s, i+1)
            if i+1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                pathcnt += decoding(s, i+2) # taking i.. i+1
            dp[i] = pathcnt
            return pathcnt
        
        return decoding(s, 0)
