class Solution:
    def twoSum(self, nums, target):
        cache = {}
        
        for i,n in enumerate(nums):
            difference = target - n
            if difference in cache:
                return [cache[difference], i]
            cache[n] = i
