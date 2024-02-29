class Solution:
    def isValid(self, s):
        stack = []

        close_to_open = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        for char in s:
            if char not in close_to_open:
                stack.append(char)
            elif not stack or stack[-1] != close_to_open[char]:
                return False
            else:
                stack.pop()
            
        return len(stack) == 0