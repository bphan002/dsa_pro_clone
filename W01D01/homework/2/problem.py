class Solution:
    def productExceptSelf(self, nums):
        # Remove pass and write code here
    # '''
    #     ## **Example 1:**
    #     **Input:** nums = [1,2,3,4]
    #     **Output:** [24,12,8,6]

    #     [1,1,2,6]
    #     [1,4,12,24]

        
    # '''
        prefix = []
        postfix = []
        res = []
        cache = 1
    
        for num in nums:
            prefix.append(cache)
            cache *=num
            
        print(prefix)

        cache = 1

        for i in range(len(nums)-1,-1,-1):
            postfix.append(cache)
            cache *= nums[i]


        for i in range(len(prefix)):
            res.append(prefix[i]*postfix[len(postfix)-i-1])
        print(res)
        return res
initial = Solution()
initial.productExceptSelf([-1,1,0,-3,3])
