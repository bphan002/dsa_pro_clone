import math

class Solution:
    def evalRPN(self, tokens):
        stack = []
        
        for op in tokens:
            
            if op in {"+", "-", "*", "/"}:
                second = stack.pop()
                first = stack.pop()
                
                if op == "+":
                    stack.append(first+second)
                elif op == "-":
                    stack.append(first-second)
                elif op == "*":
                    stack.append(first*second)
                else:
                    res = first/second
                    if res >= 0:
                        stack.append(math.floor(res))
                    else:
                        stack.append(math.ceil(res))
            else:
                stack.append(int(op))            
        
        return stack[0]