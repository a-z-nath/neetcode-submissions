class Solution:
    dp = []
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def solve(remaining):
            # Base cases
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            
            # If already computed
            if remaining in memo:
                return memo[remaining]
            
            min_coins = float('inf')
            
            for coin in coins:
                result = solve(remaining - coin)
                min_coins = min(min_coins, 1 + result)
            
            memo[remaining] = min_coins
            return min_coins
        
        ans = solve(amount)
        return ans if ans != float('inf') else -1