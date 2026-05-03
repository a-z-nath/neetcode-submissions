class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # key: (i, buying)
        def makeProfit(i: int, buying: bool):
            # out bound
            if i >= len(prices):
                return 0
            # cache
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            rest = makeProfit(i+1, buying)
            if buying:
                buy = makeProfit(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, rest)
            else:
                sell = makeProfit(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, rest)
            return dp[(i, buying)]
        return makeProfit(0, True)
            