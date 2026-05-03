class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i, c in enumerate(s):
            lastIdx[c] = i
        start = end = 0
        res = []
        for i, c in enumerate(s):
            end = max(lastIdx[c], end)
            if i == end:
                res.append(end - start + 1)
                start = end = i + 1
        return res