class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            # don't use if exceed any value than target
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(target):
                if v == t[i]:
                    good.add(i)
        return len(good) == 3