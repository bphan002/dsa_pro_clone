class Solution:
    def isValid(self, s):
        paren = {
            ")": "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        for char in s:
            if char not in paren:
                stack.append(char)
            elif stack and stack[-1] == paren[char]:
                stack.pop()
        return len(stack) == 0 