class Solution:
    def maximum69Number(self, num):
        # Remove pass and write code here
        num = str(num)
        num = list(num)
        for i,digit in enumerate(num):
            if digit == '6':
                num[i] = '9'
                break
        return int(''.join(num))