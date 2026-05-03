# You are given an integer array nums where nums[i] represents the amount of money the ith 
# house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor 
# of the (i-1)th and (i+1)th house.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses 
# because the security system will automatically alert the police if two adjacent houses 
# were both broken into.

# - maximize money
# - if robber at i-th house -> cannot rob i+1 and i-1 th house

# Return the maximum amount of money you can rob without alerting the police.

# Decision;
# - going down from n-1 to 0

# state: i -> action: rob i-th house or skip i-th house
#     rob(i) -> nums[i] + rob(i-2)
#     skip(i) -> rob(i-1)
#     max(rob(i) , skip(i))

# base case: i == 0 -> return nums[i]

class Solution:
    dp = []
    def rob(self, nums: List[int]) -> int:
        self.dp = [-1 for _ in range(101)]
        def robbing(i: int) -> int:
            if i == 0:
                return nums[i]
            if i < 0:
                return 0
            if self.dp[i] != -1:
                return self.dp[i]

            skip = robbing(i-1)
            
            rob = robbing(i-2) + nums[i]
            self.dp[i] = max(rob, skip)
            return self.dp[i]
        return robbing(len(nums)-1)
