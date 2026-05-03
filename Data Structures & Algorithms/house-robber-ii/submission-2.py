# You are given an integer array nums where nums[i] represents the amount of money the 
# ith house has. The houses are arranged in a circle, i.e. the first house and the last 
# house are neighbors.
# - circular fashion orientation 
# - 0, 1, 2, 3=> 5  house here is actually 1-th house 

# You are planning to rob money from the houses, but you cannot rob two adjacent houses 
# because the security system will automatically alert the police if two adjacent houses 
# were both broken into.

# Return the maximum amount of money you can rob without alerting the police.
# -maximize rob money
# - cannot rob i +1 or i -1 if rob i.
# - cannot rob n-1 and 0 since they are neighbor.
#     - how can i stop this??

# Decision:
# - going down from n-1 to 0
# - cannot rob 0 and n-1??
#     - a variable to keep track if max has 0-th house?
    # - find rob(nums[0: n-2]) and find rob(nums[1: -1])
    #     - max of them will be the final result
# - maximize robbed money
# state: i -> action: rob i-th house or skip i-th house
#                 rob-i = nums[i] + rob(i-1)
#                 skip-i = rob(i-1)
#                 max(rob-i, skip-i)
# base case: i == base -> nums[i]
#             i < 0 -> 0
# max(rob(n-1, 1), rob(n-2, 0))

class Solution:
    dp = []

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def helper(i: int, base: int) -> int:
            if i == base:
                return nums[i]
            if i<base:
                return 0
            if self.dp[i] != -1:
                return self.dp[i]
            
            skip = helper(i-1, base)
            rob = helper(i-2, base) + nums[i]
            self.dp[i] = max(skip, rob)

            return self.dp[i]
        
        self.dp = [-1 for _ in range(101)]
        money = helper(n-1, 1)
        self.dp = [-1 for _ in range(101)]
        money = max(money, helper(n-2, 0))
        return max(nums[0], money)
