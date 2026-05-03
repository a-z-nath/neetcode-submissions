class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {len(s): True}
        def makeWordStarting(i: int) -> bool:
            if i in dp:
                return dp[i]
            for w in wordDict:
                if (i + len(w) <= n) and s[i: i + len(w)] == w:
                    if makeWordStarting(i+len(w)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return makeWordStarting(0)
