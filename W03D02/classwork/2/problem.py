class Solution:
    def canJump(self, nums):
        # Remove pass and write code here
        '''    
                                 s e 
            Input: nums = [2,3,1,1,4]
        '''
        end = len(nums) -1
        for i,jump in enumerate(range(end,-1,-1)):
            print('i', i,'jump',)
            if i + jump >= end:
                end = i
        return end == 0


  

        



        return start == 0

        