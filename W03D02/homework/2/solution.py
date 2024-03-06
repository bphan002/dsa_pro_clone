class Solution:
    def maximum69Number(self, num):
        digits = list(str(num))
        
        for i, n in enumerate(digits):
            if n == "6":
                digits[i] = "9"
                break
                
        return int("".join(digits))