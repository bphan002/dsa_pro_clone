class Solution:
    def evalRPN(self, tokens):
        # Remove pass and write code here
        
#    ["2","1","+","3","*"]
    
    #stack = 2 1 +
    #if its 2 numbers we pop right away and put it back
        stack = [int(tokens[0]), int(tokens[1])]
        # print(stack)
        my_set = set(['+','-','/','*'])
        for i in range(2,len(tokens)):
            print('curr stack', stack)
         
            if tokens[i] in my_set:
                print('tokens[i]', tokens[i])
                val_1 = stack.pop()
                val_2 = stack.pop()
                print(val_1)
                print(val_2)
                print('----')
                if tokens[i] == "+":
                    stack.append(val_1 + val_2)
                elif tokens[i] == "-":
                    stack.append(val_2 - val_1)
                elif tokens[i] == "/":
                    stack.append(int(val_2/val_1))
                else:
                    stack.append(val_2*val_1)
            else:
                stack.append(int(tokens[i]))
        res =stack.pop()
        print(res)


sol = Solution()

sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
