class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def waysOfChange(amount: int, idx: int):
            if amount == 0:
                return 1
            # out bound idx and amount
            if idx >= len(coins) or amount < 0:
                return 0
            # cache
            if (idx, amount) in dp:
                return dp[(idx,amount)]
            ways = 0
            # take i
            if amount >= coins[idx]:
                ways += waysOfChange(amount-coins[idx], idx)
            # skip i
            ways += waysOfChange(amount, idx+1)
            dp[(idx,amount)] = ways
            return dp[(idx,amount)]
        return waysOfChange(amount, 0)