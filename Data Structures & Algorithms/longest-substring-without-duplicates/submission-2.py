class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l < 2:
            return l
        counter = [0] * 128
        slow, fast = 0, 0
        res = 0
        while slow < l and fast < l:
            idx = ord(s[fast])
            while counter[idx] != 0:
                ids = ord(s[slow])
                counter[ids] -= 1
                slow += 1
            counter[idx] += 1
            res = max(fast - slow + 1, res)
            fast += 1
        return res