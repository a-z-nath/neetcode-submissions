# You are given an array of integers cost where cost[i] is the cost of taking a step
# from the ith floor of a staircase. After paying the cost, you can step to either the 
# (i + 1)th floor or the (i + 2)th floor. 
# You may choose to start at the index 0 or the index 1 floor.

# cost -> 0 .. n-1
# - to place step at i-th stair u pay cost[i]
# - can jump i+1 and i+2
# - may start from 0 or 1 for jumping
# you've to go to n-th staircase.


# Return the minimum cost to reach the top of the staircase, i.e. 
# just past the last index in cost.

# - minimum cost to jump upto n
# - sum of all cost the staircase u leave to reach n-th staircase
# - minimize this cost.

# Decision:
# - cost minimization.
# - we go down to 0 or 1 from n
# state: i-th staircase -> action: go i-1 and i-2(if i-2 >= 0) 
#                                 minimum cost between i-1 and i -2

# base case: i = 0 or 1 return cost[i]

class Solution:
    dp = []
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp = [-1 for _ in range(101)]
        stairs = len(cost)
        cost.append(0)

        def minCost(i) -> int:
            if i == 0 or i == 1:
                return cost[i]
            if self.dp[i] != -1:
                return self.dp[i]
            mncost = minCost(i - 1)
            if i - 2 >= 0:
                mncost = min(mncost, minCost(i - 2))
            
            self.dp[i] = mncost + cost[i]
            return self.dp[i]

        return minCost(stairs)
