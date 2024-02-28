class Solution:
    # This solution uses a stack without dynamic programing. It will fail the last test case
    def fib_iterative(self, n):
        if n < 2:
            return n

        stack = [(n, 0)]
        total = 0

        while stack:
            current, index = stack.pop()

            if current == 0 or current == 1:
                total += current
            else:
                stack.append((current - 1, index + 1))
                stack.append((current - 2, index + 1))

        return total
    
    # This solution uses dynamic programming to optimize the iterative solution. We will revisit this in the future.
    def fib_dp(self, n):
        if n < 2:
            return n

        prev1, prev2 = 0, 1

        for i in range(2, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current

        return prev2
    
    # This solution uses a recursion without memoization. It will fail the last test case
    def fib_recursive(self, n):
        if n < 2:
            return n
        return self.fib_recursive(n-1) + self.fib_recursive(n-2)
    
    # This solution uses memoization to optimize the recursive solution. We will revisit this concept in the future.
    def fib_recursive_with_memo(self, n, memo = {}):
        if n < 2:
            return n
        if n in memo:
            return memo[n]

        memo[n] = self.fib_recursive_with_memo(n-1) + self.fib_recursive_with_memo(n-2)
        return memo[n]