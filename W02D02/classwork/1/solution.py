class Solution:
    def backspaceCompare(self, s, t) -> bool:
        
        def build(str):
            stack = []
            
            for char in str:
                if char != "#": 
                    stack.append(char)
                elif stack:
                    stack.pop()
            return "".join(stack)
        
        return build(s) == build(t)