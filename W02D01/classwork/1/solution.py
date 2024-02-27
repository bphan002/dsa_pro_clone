class Solution:
    def minSubArrayLen(self, target, nums):

        left, total, min_sub = 0, 0, float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_sub = min(min_sub, right-left+1)
                total -= nums[left]
                left += 1

        return 0 if min_sub == float('inf') else min_sub