# You are given an integer n representing `the number of steps to reach the top of a staircase`.
# You can climb with either 1 or 2 steps at a time.
# - 1 <= n <= 45
# - jump 1 or 2 steps

# Return the number of distinct ways to climb to the top of the staircase.
# - counting
# - distinct path

# how many ways to go from 0 to n or n to 0?
# n =3
# path-1: 0 -> 1 -> 2 -> 3
# path-2: 0 -> 2 -> 3
# path-3: 0 -> 1 -> 3

# Decision:
# - we will go down n to 0
# - jump 1 or 2 step down if possible.
# n =3 both 1 and 2 step down since both is possible.

# state: n -> action: go n-1 and go n-2 if n >= 2.

# base case n == 0 => return 1.



class Solution:
    dp: List = [-1 for _ in range(100)]
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if self.dp[n] != -1:
            return self.dp[n]

        ways = self.climbStairs(n-1)
        if n >= 2:
            ways += self.climbStairs(n-2)
        self.dp[n] = ways
        return self.dp[n]
