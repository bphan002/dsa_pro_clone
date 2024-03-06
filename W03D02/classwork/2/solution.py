class Solution:
    def canJump(self, nums):
        target = len(nums) - 1

        for curr in range(len(nums)-1, -1, -1):
            if curr + nums[curr] >= target:
                target = curr

        return target == 0