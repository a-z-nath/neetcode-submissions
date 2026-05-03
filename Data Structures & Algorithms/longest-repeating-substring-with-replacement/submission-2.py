class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n, c =len(s), s[0]
        l, r= 0, 0
        res = 0
        maxf = 0
        counter = defaultdict(int)
        while l < n and r < n:
            counter[s[r]] += 1
            maxf = max(maxf, counter[s[r]])
            while ((r-l + 1) - maxf) > k:
                counter[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
            r += 1

        return res