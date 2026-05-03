class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timer(k: int) -> int:
            time = 0
            for pile in piles:
                time += pile // k if pile % k == 0 else 1 + pile // k
            return time
        mnA, mxA = 1, max(piles)
        res = -1
        while mnA <= mxA:
            midA = (mnA + mxA) // 2
            if timer(midA) <= h:
                res = midA
                mxA = midA - 1
            else:
                mnA = midA + 1
        return res