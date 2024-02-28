class Solution:
    # This solution uses a stack without dynamic programing. It will fail the last test case
    def climbStairs_iterative(self, n):
        if n == 0 or n == 1:
            return 1

        stack = [(n, 0)]
        total = 0

        while stack:
            current, index = stack.pop()

            if current == 0 or current == 1:
                total += 1
            else:
                stack.append((current - 1, index + 1))
                stack.append((current - 2, index + 1))

        return total
    
    # This solution uses dynamic programming to optimize the iterative solution. We will revisit this in the future.
    def climbStairs_dp(self, n):
        if n == 0 or n == 1:
            return 1

        prev1, prev2 = 1, 1

        for i in range(2, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current

        return prev2
    
    # This solution uses a recursion without memoization. It will fail the last test case
    def climbStairs_recursive(self, n):
        if n == 0 or n == 1:
            return 1
        return self.climbStairs_recursive(n-1) + self.climbStairs_recursive(n-2)
    
    # This solution uses memoization to optimize the recursive solution. We will revisit this concept in the future.
    def climbStairs_recursive_with_memo(self, n, memo = {}):
        if n == 0 or n == 1:
            return 1
        if n in memo:
            return memo[n]

        memo[n] = self.climbStairs_recursive_with_memo(n-1) + self.climbStairs_recursive_with_memo(n-2)
        return memo[n]