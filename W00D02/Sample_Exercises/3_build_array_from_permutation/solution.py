class Solution:
    def buildArray(self, nums):
        N = len(nums)
        res = [None]*N
        
        for i in range(N):
            res[i] = nums[nums[i]]
        
        return res