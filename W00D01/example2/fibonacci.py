class Solution:
    def fibonacci(self, n, memo={}):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in memo:
            return memo[n]
        
        memo[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
        return memo[n]