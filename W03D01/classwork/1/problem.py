class Solution:
    def search(self, nums, target):
        # Remove pass and write code here
        left = 0
        right = len(nums) - 1

        while left <= right:
            midpoint = left + ((right - left)//2)
            if nums[midpoint] > target:
                right = midpoint - 1
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                return midpoint
        
        return -1