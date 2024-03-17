class Solution:
    def climbStairs(self, n, memo = {}):
        # Remove pass and write code here
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return 1
        
        memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        return memo[n]