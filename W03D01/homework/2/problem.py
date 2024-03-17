class Solution:
    def findPeakElement(self, nums):
        # Remove pass and write code here
    
        left = 0

        right = len(nums) - 1

    

        while (left <= right):
            mid = left + ((right-left//2))
            if mid == 0 and nums[mid] > nums[mid+1]:
                return mid
            if mid == len(nums)-1 and nums[mid] > nums[mid -1]:
                return mid
            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid
            elif nums[mid] > nums[mid-1]:
                left = mid + 1
            else:
                right = mid - 1