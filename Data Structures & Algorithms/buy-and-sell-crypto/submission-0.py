class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l <=1:
            return 0
        
        s, f = 0, 1
        ans = 0
        while f < l:
            ans = max(ans, prices[f] - prices[s])
            if prices[s] > prices[f]:
                s = f
                f += 1
            else:
                f += 1
        return ans