class Solution:
    def minSubArrayLen(self, target, nums):
        # Remove pass and write code here
        left = 0
        sum = 0
        min_sub = float('inf')

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                min_sub = min(min_sub, right-left + 1)
                sum -= nums[left]
                left +=1

        return 0 if min_sub == float('inf') else min_sub
