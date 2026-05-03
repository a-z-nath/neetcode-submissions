class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on  answer
        # ans = [1, max(piles)]

        def helper(k: int):
            hour = 0
            for x in piles:
                hour += x // k
                hour += (1 if x % k else 0)
            return hour

        low, high = 1, max(piles)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            esthour = helper(mid)
            if esthour <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans
