class Solution:
    def fizzBuzz(self, n):
        res = []
        
        for i in range(1, n+1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            
            if len(s) == 0:
                s = str(i)
            
            res.append(s)
        return res