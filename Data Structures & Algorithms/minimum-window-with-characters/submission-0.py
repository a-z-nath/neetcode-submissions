class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        cntT, cntS = Counter(t), Counter()
        l, r = 0, 0
        have, need = 0, len(cntT)
        res, resLen = [-1, -1], float("inf")
        for r in range(len(s)):
            cntS[s[r]] += 1
            if s[r] in cntT and cntT[s[r]] == cntS[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                cntS[s[l]] -= 1
                if s[l] in cntT and cntS[s[l]] < cntT[s[l]]:
                    have -= 1
                l += 1
            
        l, r = res
        return s[l: r+1] if resLen != float("inf") else ""
