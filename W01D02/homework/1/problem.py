class Solution:
    def twoSum(self, nums, target):
        # Remove pass and write code here
        hash = {}

        for i in range(len(nums)):
            currNum = nums[i]
            compliment = target - currNum
            if compliment in hash:
                return i, hash[compliment]
            hash[currNum] = i