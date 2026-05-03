class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        seHash = {}
        for i, c in enumerate(s):
            if c in seHash:
                seHash[c][1] = i
            else:
                seHash[c] = [i, i]
        print(seHash)
        start, end = 0, 0
        res = []
        for i, c in enumerate(s):
            s, e = seHash[c]
            end = max(e, end)
            if i == end:
                res.append(end - start + 1)
                start = end = i + 1
        return res